## Weather MCP Server

This project exposes National Weather Service data through an MCP server using `FastMCP` and `httpx`.

### What This Provides

- An MCP server named `weather` running over STDIO.
- Two tools:
	- `get_alerts(state: str)`
	- `get_forecast(latitude: float, longitude: float)`
- A simple `uv`-managed Python project with a local `.venv`.

### Project Layout

```
weather/
	README.md
	pyproject.toml
	weather.py
	main.py
.vscode/
	mcp.json
```

### Code Overview

The MCP server is implemented in `weather.py`:

- Creates a `FastMCP` server instance: `mcp = FastMCP("weather")`.
- Uses `httpx.AsyncClient` to call the NWS API with a custom `User-Agent`.
- Exposes two MCP tools with `@mcp.tool()` decorators:
	- `get_alerts(state)` fetches active alerts for a US state.
	- `get_forecast(latitude, longitude)` fetches the 5-period forecast.
- Runs the server in `main()` with `mcp.run(transport="stdio")`.

`main.py` is a placeholder file and is not used by the MCP server.

### Dependencies

Defined in `pyproject.toml`:

- `mcp[cli]`
- `httpx`

### Local Environment

The `.venv` is located in:

```
D:\my first mcp\weather\.venv
```

Activate it (PowerShell):

```powershell
Set-Location "D:\my first mcp\weather"
.\.venv\Scripts\Activate.ps1
```

Install dependencies with `uv`:

```powershell
uv add "mcp[cli]" httpx
```

### MCP Configuration

VS Code MCP server config is in `.vscode/mcp.json` and runs the server with `uv`:

```jsonc
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
```

This ensures `uv` runs the script from the correct project and picks up the local environment.

### Running Manually

From the project folder:

```powershell
Set-Location "D:\my first mcp\weather"
uv run python weather.py
```

### MCP Tools

`get_alerts(state: str)`
- Returns active alerts for a US state (e.g., `CA`, `NY`).

`get_forecast(latitude: float, longitude: float)`
- Returns a short forecast for the given coordinates.

### Troubleshooting

- If VS Code shows import errors, re-select the interpreter:
	- `Python: Select Interpreter` -> `D:\my first mcp\weather\.venv\Scripts\python.exe`.
- If the server prints the `uv` help text, the MCP config is missing the `run` args.
- If `weather.py` cannot be found, ensure you run from the `weather` project or use the full path.

---

# Weather MCP Server (Python)

A beginner-friendly Weather MCP (Model Context Protocol) Server built using Python, FastMCP, and the National Weather Service (NWS) API.

This project was created to learn the fundamentals of MCP (Model Context Protocol), including MCP server development, tool creation, VS Code integration, and external API communication.

---

## Project Overview

This MCP server exposes weather-related tools that can be discovered and invoked by MCP-compatible clients such as Visual Studio Code with GitHub Copilot.

The server communicates with the National Weather Service (NWS) API and provides weather forecasts and weather alerts through MCP tools.

---

## Features

### Weather Alerts Tool

Retrieve active weather alerts for a U.S. state.

**Input**

- State Code (Example: NY, CA, TX)

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
│
├── weather.py
├── pyproject.toml
├── uv.lock
├── README.md
├── .gitignore
└── .vscode/
		└── mcp.json
```

---

## MCP Architecture

```text
GitHub Copilot (VS Code)
					 │
					 ▼
			MCP Client
					 │
					 ▼
		 Weather MCP Server
					 │
					 ▼
 National Weather Service API
					 │
					 ▼
			Weather Data
```

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

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/mcp-weather-server-python.git
cd mcp-weather-server-python
```

### Create Virtual Environment

```bash
uv venv
```

### Activate Environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
uv sync
```

or

```bash
uv add "mcp[cli]" httpx
```

---

## Running the MCP Server

```bash
uv run weather.py
```

The server uses STDIO transport and waits for incoming MCP requests from compatible clients.

---

## VS Code Integration

Create:

```text
.vscode/mcp.json
```

Example configuration:

```json
{
	"servers": {
		"weather": {
			"command": "uv",
			"args": [
				"--directory",
				"YOUR_PROJECT_PATH",
				"run",
				"weather.py"
			]
		}
	}
}
```

---

## Learning Outcomes

Through this project I learned:

- MCP Fundamentals
- MCP Client-Server Architecture
- FastMCP
- Tool Registration using @mcp.tool()
- STDIO Transport
- External API Integration
- VS Code MCP Integration
- GitHub Copilot Tool Calling
- MCP Tool Discovery
- MCP Server Deployment Concepts

---

## Documentation & Learning Resources

Official MCP Documentation:

https://modelcontextprotocol.io

Python SDK Documentation:

https://modelcontextprotocol.io/quickstart/server

MCP Python SDK GitHub Repository:

https://github.com/modelcontextprotocol/python-sdk

VS Code MCP Documentation:

https://code.visualstudio.com/docs/copilot/chat/mcp-servers

National Weather Service API:

https://www.weather.gov/documentation/services-web-api

---

## Future Improvements

- Add Weather by City Name
- Add Historical Weather Data
- Add Weather Maps
- Add Multi-country Weather Support
- Add Resource Support
- Integrate with LLM Agents
- Integrate with RAG Pipelines
- Deploy as Remote MCP Server

---

