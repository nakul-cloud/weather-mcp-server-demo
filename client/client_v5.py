import asyncio
import json
import os
from dotenv import load_dotenv
import os

load_dotenv()

from google import genai

from mcp import ClientSession
from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)


# -------------------------------
# Gemini Setup
# -------------------------------

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# -------------------------------
# City Mapping
# -------------------------------

CITY_COORDS = {
    "new york": (40.7128, -74.0060),
    "los angeles": (34.0522, -118.2437),
    "chicago": (41.8781, -87.6298),
    "houston": (29.7604, -95.3698),
    "miami": (25.7617, -80.1918),
}


# -------------------------------
# MCP Tool Wrappers
# -------------------------------

async def call_forecast(
    session,
    latitude,
    longitude
):

    result = await session.call_tool(
        "get_forecast",
        {
            "latitude": latitude,
            "longitude": longitude
        }
    )

    output = ""

    for content in result.content:
        if hasattr(content, "text"):
            output += content.text + "\n"

    return output


async def call_alerts(
    session,
    state
):

    result = await session.call_tool(
        "get_alerts",
        {
            "state": state.upper()
        }
    )

    output = ""

    for content in result.content:
        if hasattr(content, "text"):
            output += content.text + "\n"

    return output


# -------------------------------
# Gemini Tool Selection
# -------------------------------

def ask_gemini_for_tool(user_query):

    prompt = f"""
You are an MCP routing assistant.

Available MCP tools:

1. get_forecast
   Inputs:
   - city

2. get_alerts
   Inputs:
   - state

Return ONLY JSON.

Examples:

User:
weather in New York

Output:
{{"tool":"get_forecast","city":"new york"}}

User:
alerts for NY

Output:
{{"tool":"get_alerts","state":"NY"}}

User request:
{user_query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()


# -------------------------------
# Gemini Explanation
# -------------------------------

def explain_weather(
    user_question,
    weather_data
):

    prompt = f"""
User question:

{user_question}

Weather data:

{weather_data}

Answer naturally.
Give a helpful explanation.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# -------------------------------
# Main
# -------------------------------

async def main():

    server_params = StdioServerParameters(
        command="uv",
        args=[
            "--directory",
            r"D:\my first mcp\weather",
            "run",
            "server\\weather.py"
        ]
    )

    async with stdio_client(server_params) as (
        read_stream,
        write_stream
    ):

        async with ClientSession(
            read_stream,
            write_stream
        ) as session:

            await session.initialize()

            print("\n" + "=" * 60)
            print("       MCP WEATHER AGENT V5")
            print("=" * 60)

            print(
                "\nExamples:"
            )

            print(
                "What's the weather in New York?"
            )

            print(
                "Should I carry an umbrella tomorrow in Chicago?"
            )

            print(
                "Any alerts for NY?"
            )

            print(
                "\nType 'exit' to quit."
            )

            while True:

                user_query = input(
                    "\nYou: "
                ).strip()

                if not user_query:
                    continue

                if user_query.lower() == "exit":
                    break

                try:

                    tool_response = ask_gemini_for_tool(
                        user_query
                    )

                    print(
                        "\nGemini Tool Decision:"
                    )

                    print(tool_response)

                    tool_data = json.loads(
                        tool_response
                    )

                    tool_name = tool_data.get(
                        "tool"
                    )

                    if tool_name == "get_forecast":

                        city = tool_data.get(
                            "city",
                            ""
                        ).lower()

                        if city not in CITY_COORDS:

                            print(
                                f"\nUnknown city: {city}"
                            )

                            continue

                        latitude, longitude = (
                            CITY_COORDS[city]
                        )

                        weather_data = (
                            await call_forecast(
                                session,
                                latitude,
                                longitude
                            )
                        )

                    elif tool_name == "get_alerts":

                        state = tool_data.get(
                            "state"
                        )

                        weather_data = (
                            await call_alerts(
                                session,
                                state
                            )
                        )

                    else:

                        print(
                            "\nNo valid tool selected."
                        )

                        continue

                    print(
                        "\nRaw MCP Result:\n"
                    )

                    print(weather_data)

                    explanation = (
                        explain_weather(
                            user_query,
                            weather_data
                        )
                    )

                    print(
                        "\nAgent Response:\n"
                    )

                    print(explanation)

                except Exception as e:

                    print(
                        f"\nError: {e}"
                    )


if __name__ == "__main__":
    asyncio.run(main())

