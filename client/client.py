import asyncio

from mcp import ClientSession
from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)


async def list_tools(session):

    tools = await session.list_tools()

    print("\nAvailable Tools:\n")

    for tool in tools.tools:
        print(f"- {tool.name}")


async def show_tool_details(session):

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
            print("      MCP WEATHER ASSISTANT V3")
            print("=" * 60)

            print("\nCommands:")
            print("tools")
            print("details")
            print("forecast <latitude> <longitude>")
            print("alerts <state>")
            print("exit")

            while True:

                user_input = input(
                    "\nYou: "
                ).strip()

                if not user_input:
                    continue

                if user_input.lower() == "exit":

                    print("\nGoodbye!")
                    break

                elif user_input.lower() == "tools":

                    await list_tools(session)

                elif user_input.lower() == "details":

                    await show_tool_details(session)

                elif user_input.lower().startswith(
                    "forecast"
                ):

                    parts = user_input.split()

                    if len(parts) != 3:

                        print(
                            "\nUsage:"
                            "\nforecast <lat> <lon>"
                        )

                        continue

                    try:

                        latitude = float(parts[1])
                        longitude = float(parts[2])

                        await call_forecast(
                            session,
                            latitude,
                            longitude
                        )

                    except ValueError:

                        print(
                            "\nLatitude and Longitude "
                            "must be numbers."
                        )

                elif user_input.lower().startswith(
                    "alerts"
                ):

                    parts = user_input.split()

                    if len(parts) != 2:

                        print(
                            "\nUsage:"
                            "\nalerts NY"
                        )

                        continue

                    state = parts[1]

                    await call_alerts(
                        session,
                        state
                    )

                else:

                    print(
                        "\nUnknown command."
                    )

                    print(
                        "\nTry:"
                        "\n tools"
                        "\n details"
                        "\n forecast 40.7128 -74.0060"
                        "\n alerts NY"
                        "\n exit"
                    )


if __name__ == "__main__":
    asyncio.run(main())