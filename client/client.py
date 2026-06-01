 
import asyncio

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


async def get_forecast(session):
    """Call get_forecast MCP tool"""

    try:
        latitude = float(
            input("\nEnter Latitude: ")
        )

        longitude = float(
            input("Enter Longitude: ")
        )

    except ValueError:
        print("\nInvalid coordinates.")
        return

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


async def get_alerts(session):
    """Call get_alerts MCP tool"""

    state = input(
        "\nEnter US State Code (NY, CA, TX etc): "
    ).strip().upper()

    print("\nFetching Alerts...\n")

    result = await session.call_tool(
        "get_alerts",
        {
            "state": state
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

            print("\nInitializing MCP Session...")

            await session.initialize()

            print("\nConnected Successfully!")

            while True:

                print("\n" + "=" * 50)
                print("         MCP WEATHER CLIENT V2")
                print("=" * 50)

                print("1. List Available Tools")
                print("2. Get Weather Forecast")
                print("3. Get Weather Alerts")
                print("4. Show Tool Details")
                print("5. Exit")

                choice = input(
                    "\nEnter Choice: "
                ).strip()

                if choice == "1":
                    await list_tools(session)

                elif choice == "2":
                    await get_forecast(session)

                elif choice == "3":
                    await get_alerts(session)

                elif choice == "4":
                    await show_tool_details(session)

                elif choice == "5":
                    print("\nGoodbye!")
                    break

                else:
                    print(
                        "\nInvalid choice. Please try again."
                    )


if __name__ == "__main__":
    asyncio.run(main())
