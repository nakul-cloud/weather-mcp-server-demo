import asyncio

from mcp import ClientSession
from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)


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

            print("\nInitializing MCP Session...\n")

            await session.initialize()

            tools = await session.list_tools()

            print("Available Tools:\n")

            for tool in tools.tools:
                print(f"- {tool.name}")

            print("\nCalling get_forecast tool...\n")

            result = await session.call_tool(
                "get_alerts",
                {
                    "latitude": 40.7128,
                    "longitude": -74.0060
                }
            )

            print("Forecast Result:\n")
            for content in result.content:
                if hasattr(content, "text"):
                    print(content.text)


if __name__ == "__main__":
    asyncio.run(main())