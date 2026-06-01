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


async def get_forecast(session):

    try:
        latitude = float(input("Enter Latitude: "))
        longitude = float(input("Enter Longitude: "))
    except ValueError:
        print("Invalid coordinates.")
        return

    print("\nFetching Forecast...\n")

    result = await session.call_tool(
        "get_forecast",
        {
            "latitude": latitude,
            "longitude": longitude
        }
    )

    for content in result.content:
        if hasattr(content, "text"):
            print(content.text)


async def get_alerts(session):

    state = input(
        "Enter US State Code (NY, CA, TX etc): "
    ).strip().upper()

    print("\nFetching Alerts...\n")

    result = await session.call_tool(
        "get_alerts",
        {
            "state": state
        }
    )

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

            while True:

                print("\n" + "=" * 40)
                print("      MCP WEATHER CLIENT")
                print("=" * 40)

                print("1. List Available Tools")
                print("2. Get Weather Forecast")
                print("3. Get Weather Alerts")
                print("4. Exit")

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
                    print("\nGoodbye!")
                    break

                else:
                    print(
                        "\nInvalid choice. Try again."
                    )


if __name__ == "__main__":
    asyncio.run(main())