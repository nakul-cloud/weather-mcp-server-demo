# Weather MCP Server (Python)

A beginner-friendly Weather MCP (Model Context Protocol) Server built using Python, FastMCP, and the National Weather Service (NWS) API.

This project was created to learn the fundamentals of MCP, including MCP server development, tool creation, VS Code integration, and external API communication.

---

## Project Overview

This MCP server exposes weather-related tools that can be discovered and invoked by MCP-compatible clients such as Visual Studio Code with GitHub Copilot. It communicates with the National Weather Service (NWS) API and provides weather forecasts and weather alerts through MCP tools.

---

## Features

### Weather Alerts Tool

Retrieve active weather alerts for a U.S. state.

**Input**

- State code (example: NY, CA, TX)

**Output**

- Active weather alerts
- Alert severity
- Affected areas
- Instructions and descriptions

---

### Weather Forecast Tool

Retrieve weather forecast information using geographic coordinates.

**Input**

- Latitude
- Longitude

**Output**

- Temperature
- Wind information
- Detailed weather forecast
- Multi-period forecast summary

---

## Tech Stack

- Python 3.11
- MCP Python SDK
- FastMCP
- HTTPX
- Visual Studio Code
- GitHub Copilot
- National Weather Service API

---

## Project Structure

```text
weather/
├── weather.py
├── pyproject.toml
├── uv.lock
├── README.md
├── main.py
└── .vscode/
    └── mcp.json
```

---

## MCP Architecture

```text
GitHub Copilot (VS Code)
           |
           v
      MCP Client
           |
           v
     Weather MCP Server
           |
           v
 National Weather Service API
           |
           v
      Weather Data
```

---

## Code Overview

The MCP server is implemented in `weather.py`:

- Creates a `FastMCP` server instance: `mcp = FastMCP("weather")`.
- Uses `httpx.AsyncClient` to call the NWS API with a custom `User-Agent`.
- Exposes two MCP tools with `@mcp.tool()` decorators:
  - `get_alerts(state)` fetches active alerts for a US state.
  - `get_forecast(latitude, longitude)` fetches the 5-period forecast.
- Runs the server in `main()` with `mcp.run(transport="stdio")`.

`main.py` is a placeholder file and is not used by the MCP server.

---

## Available MCP Tools

### get_alerts

Returns active weather alerts for a specified U.S. state.

Example:

```python
get_alerts("NY")
```

---

### get_forecast

Returns weather forecast information for a location.

Example:

```python
get_forecast(
    latitude=40.7128,
    longitude=-74.0060
)
```

---

## Local Environment

The `.venv` is located at:

```
D:\my first mcp\weather\.venv
```

Activate it (PowerShell):

```powershell
Set-Location "D:\my first mcp\weather"
.\.venv\Scripts\Activate.ps1
```

---

## Installation

### Clone Repository (optional)

```bash
git clone https://github.com/YOUR_USERNAME/mcp-weather-server-python.git
cd mcp-weather-server-python
```

### Create Virtual Environment

```bash
uv venv
```

### Install Dependencies

```bash
uv sync
```

or

```bash
uv add "mcp[cli]" httpx
```

Dependencies are defined in `pyproject.toml`:

- `mcp[cli]`
- `httpx`

---

## Running the MCP Server

From the project folder:

```powershell
Set-Location "D:\my first mcp\weather"
uv run python weather.py
```

The server uses STDIO transport and waits for incoming MCP requests from compatible clients.

---

## VS Code MCP Integration

The MCP server config lives at `.vscode/mcp.json`. Current working config:

```json
{
  "servers": {
    "weather": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "run",
        "--project",
        "weather",
        "python",
        "weather/weather.py"
      ]
    }
  },
  "inputs": []
}
```

This ensures `uv` runs the script from the correct project and picks up the local environment.

---

## Troubleshooting

- If VS Code shows import errors, re-select the interpreter:
  - `Python: Select Interpreter` -> `D:\my first mcp\weather\.venv\Scripts\python.exe`.
- If the server prints the `uv` help text, the MCP config is missing the `run` args.
- If `weather.py` cannot be found, ensure you run from the `weather` project or use the full path.

---

## Learning Outcomes

Through this project I learned:

- MCP fundamentals
- MCP client-server architecture
- FastMCP
- Tool registration using `@mcp.tool()`
- STDIO transport
- External API integration
- VS Code MCP integration
- GitHub Copilot tool calling
- MCP tool discovery
- MCP server deployment concepts

---

## Documentation and Learning Resources

- https://modelcontextprotocol.io
- https://modelcontextprotocol.io/quickstart/server
- https://github.com/modelcontextprotocol/python-sdk
- https://code.visualstudio.com/docs/copilot/chat/mcp-servers
- https://www.weather.gov/documentation/services-web-api

---

## Future Improvements

- Add weather by city name
- Add historical weather data
- Add weather maps
- Add multi-country weather support
- Add resource support
- Integrate with LLM agents
- Integrate with RAG pipelines
- Deploy as a remote MCP server

---

## Author

Nakul Jadhav

Learning Project: First MCP Server using Python and FastMCP

