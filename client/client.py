import asyncio
import re

from mcp import ClientSession
from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)


async def list_tools(session):
    """List all available MCP tools"""

    tools = await session.list_tools()

    print("\nAvailable Tools:\n")

    for tool in tools.tools:
        print(f"- {tool.name}")


async def show_tool_details(session):
    """Display tool metadata and schema"""

    tools = await session.list_tools()

    print("\nTool Details:\n")

    for tool in tools.tools:

        print("=" * 60)

        print(f"Tool Name: {tool.name}")

        if hasattr(tool, "description"):
            print(f"\nDescription:\n{tool.description}")

        if hasattr(tool, "inputSchema"):
            print(f"\nInput Schema:\n{tool.inputSchema}")

        print("=" * 60)


async def call_forecast(
    session,
    latitude,
    longitude
):
    """Call forecast tool"""

    print("\nFetching Forecast...\n")

    result = await session.call_tool(
        "get_forecast",
        {
            "latitude": latitude,
            "longitude": longitude
        }
    )

    print("\nForecast Result:\n")

    for content in result.content:
        if hasattr(content, "text"):
            print(content.text)


async def call_alerts(
    session,
    state
):
    """Call alerts tool"""

    print("\nFetching Alerts...\n")

    result = await session.call_tool(
        "get_alerts",
        {
            "state": state.upper()
        }
    )

    print("\nAlert Result:\n")

    for content in result.content:
        if hasattr(content, "text"):
            print(content.text)


def detect_intent(user_input: str):
    """
    Simple intent detection engine
    """

    text = user_input.lower().strip()

    # Tools

    if any(
        phrase in text
        for phrase in [
            "tool",
            "tools",
            "available tools",
            "list tools"
        ]
    ):
        return "tools"

    # Details

    if any(
        phrase in text
        for phrase in [
            "detail",
            "details",
            "schema",
            "tool details"
        ]
    ):
        return "details"

    # Forecast

    weather_pattern = (
        r"(-?\d+\.\d+)\s+(-?\d+\.\d+)"
    )

    weather_match = re.search(
        weather_pattern,
        text
    )

    if weather_match:

        lat = float(
            weather_match.group(1)
        )

        lon = float(
            weather_match.group(2)
        )

        return (
            "forecast",
            lat,
            lon
        )

    # Alerts

    alert_patterns = [
        r"alerts?\s+for\s+([a-z]{2})",
        r"alerts?\s+([a-z]{2})",
        r"check\s+alerts?\s+([a-z]{2})"
    ]

    for pattern in alert_patterns:

        match = re.search(
            pattern,
            text
        )

        if match:

            return (
                "alerts",
                match.group(1).upper()
            )

    return "unknown"


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
            print("         MCP WEATHER ASSISTANT V4")
            print("=" * 60)

            print("\nExamples:")
            print("• list tools")
            print("• show tool details")
            print("• weather 40.7128 -74.0060")
            print("• forecast 34.0522 -118.2437")
            print("• alerts for NY")
            print("• check alerts CA")
            print("• exit")

            while True:

                user_input = input(
                    "\nYou: "
                ).strip()

                if not user_input:
                    continue

                if user_input.lower() == "exit":

                    print("\nGoodbye!")
                    break

                intent = detect_intent(
                    user_input
                )

                if intent == "tools":

                    await list_tools(
                        session
                    )

                elif intent == "details":

                    await show_tool_details(
                        session
                    )

                elif isinstance(
                    intent,
                    tuple
                ):

                    if intent[0] == "forecast":

                        await call_forecast(
                            session,
                            intent[1],
                            intent[2]
                        )

                    elif intent[0] == "alerts":

                        await call_alerts(
                            session,
                            intent[1]
                        )

                else:

                    print(
                        "\nI couldn't understand that request."
                    )

                    print(
                        "\nTry examples like:"
                    )

                    print(
                        "\nweather 40.7128 -74.0060"
                    )

                    print(
                        "alerts for NY"
                    )

                    print(
                        "list tools"
                    )

                    print(
                        "show tool details"
                    )

                    print(
                        "exit"
                    )


if __name__ == "__main__":
    asyncio.run(main())

