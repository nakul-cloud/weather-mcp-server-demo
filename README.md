# Weather MCP Server (Python + Gemini + MCP)

A hands-on learning project built to understand the Model Context Protocol (MCP), MCP server development, MCP client development, tool calling, and AI agent architectures.

The project evolved from a basic MCP weather server into a Gemini-powered AI agent capable of:

Discovering MCP tools
Calling MCP tools dynamically
Resolving locations worldwide
Retrieving weather forecasts globally
Generating natural language responses using Gemini 2.5 Flash

---

## Project Overview

This MCP server exposes weather-related tools that can be discovered and invoked by MCP-compatible clients such as Visual Studio Code with GitHub Copilot. It communicates with the National Weather Service (NWS) API and provides weather forecasts and weather alerts through MCP tools selection using NLP and External API's.

This repository demonstrates the complete MCP workflow:

```text
User
 │
 ▼
Gemini 2.5 Flash
 │
 ▼
Tool Selection
 │
 ▼
MCP Client
 │
 ▼
MCP Server
 │
 ▼
External APIs
 │
 ▼
Weather Data
 │
 ▼
AI Generated Response
``` 

The project is divided into two major components:

Client

Located in:
```text

client/
```
Contains multiple MCP client implementations developed incrementally from V1 to V5.1.

Key concepts explored:

- MCP Session Initialization
- Tool Discovery
- Tool Inspection
- Tool Invocation
- Intent Detection
- Gemini Tool Selection
- Geocoding Integration
- AI Agent Workflows

See:

client/README.md

for detailed client evolution and implementation notes.

Server 

```text
Located in:
```

server/

Contains multiple MCP weather server implementations.

Key concepts explored:

FastMCP
- MCP Tool Development
- External API Integration
- Weather Forecast Services
- Global Weather Support
- MCP Server Architecture

See:

server/README.md

for detailed server documentation.

### Current Architecture (V5.2)
```text
User
 │
 ▼
Gemini 2.5 Flash
 │
 ▼
Tool Selection
 │
 ▼
Open-Meteo Geocoding API
 │
 ▼
Coordinates
 │
 ▼
Weather MCP Server
 │
 ▼
Open-Meteo Forecast API
 │
 ▼
Weather Data
 │
 ▼
Gemini Explanation
 │
 ▼
Final Response
```
---

## Features
AI-Powered Weather Assistant

Ask questions such as:

What's the weather in New York?

Will it rain tomorrow in London?

Do I need a jacket in Paris?

Should I carry an umbrella in Tokyo?

The system automatically:

1. Understands the request using Gemini
2. Selects the appropriate MCP tool
3. Resolves the location
4. Retrieves weather information
5. Generates a human-friendly response

## Client and Server Evolution

### Client Evolution

```text
V1  Tool Discovery

V2  Tool Inspection

V3  Interactive Tool Invocation

V4  Intent-Based Routing

V5  Gemini Tool Selection

V5.1 Global Geocoding + AI Agent
```

### Server Evolution

```text
weather.py
National Weather Service (NWS)

↓

weather_v5_2.py
Open-Meteo Forecast API
```



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
Global Weather Forecasting

Supported worldwide through:

Open-Meteo Geocoding API
Open-Meteo Forecast API

Example locations:

Ahmedabad
New York
London
Tokyo
Sydney
Paris
Berlin
Dubai
Singapore

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
- Google GenAI SDk
- Open-Meteo Geocoding API
- Open-Meteo Forecast API
- Gemini 2.5 Flash

---

## Project Structure

```text
weather/
├── client/
│   ├── client_v1.py
│   ├── client_v2.py
│   ├── client_v3.py
│   ├── client_v4.py
│   ├── client_v5.py
│   ├── client_v5_1.py
│   └── README.md
│
├── server/
│   ├── weather.py
│   ├── weather_v5_2.py
│   └── README.md
│
├── .vscode/
│   └── mcp.json
│
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Folder Overview

### client/

Contains multiple MCP client implementations developed throughout the learning journey.

| Version | Description                                |
| ------- | ------------------------------------------ |
| V1      | MCP Tool Discovery Client                  |
| V2      | MCP Tool Inspection Client                 |
| V3      | Interactive Command-Based Client           |
| V4      | Intent-Based MCP Client                    |
| V5      | Gemini-Powered MCP Agent                   |
| V5.1    | Gemini Agent with Global Geocoding Support |

Concepts explored:

* MCP Session Management
* Tool Discovery
* Tool Inspection
* Tool Invocation
* Intent Detection
* Gemini Tool Calling
* Geocoding APIs
* Agent Workflows

Detailed documentation:

```text
client/README.md
```

---

### server/

Contains MCP weather server implementations.

| Version         | Description                                                      |
| --------------- | ---------------------------------------------------------------- |
| weather.py      | Original Weather MCP Server using National Weather Service (NWS) |
| weather_v5_2.py | Global Weather MCP Server using Open-Meteo Forecast API          |

Concepts explored:

* FastMCP
* Tool Development
* Weather APIs
* External API Integration
* Global Weather Support
* MCP Server Architecture

Detailed documentation:

```text
server/README.md
```

---

### .vscode/

Contains MCP configuration files used by VS Code and GitHub Copilot.

---

### pyproject.toml and uv.lock

Dependency management files used by the project.

---

### .env

Stores environment variables such as:

```text
GEMINI_API_KEY
```

Used by the Gemini-powered MCP client.


## MCP Architecture

```text
User
 │
 ▼
Gemini 2.5 Flash
 │
 ▼
MCP Client
 │
 ▼
MCP Server
 │
 ▼
Open-Meteo Forecast API
 │
 ▼
Weather Data
 │
 ▼
Gemini Generated Response
```

## Code Overview

The repository currently contains two MCP server implementations:

- `server/weather.py` – Original Weather MCP Server using the National Weather Service (NWS) API.
- `server/weather_v5_2.py` – Global Weather MCP Server using the Open-Meteo Forecast API.

The latest version (`weather_v5_2.py`) powers the Gemini-based weather agent and supports worldwide weather forecasting.

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
The tools are exposed through FastMCP and can be invoked by:

- VS Code GitHub Copilot
- Custom Python MCP Clients
- Gemini-powered MCP Agent Clients

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
uv add "mcp[cli]" httpx google-genai python-dotenv
```

Dependencies are defined in pyproject.toml:

- mcp[cli]
- httpx
- google-genai
- python-dotenv

---

## Running the MCP Server

From the project folder:

```powershell
Set-Location "D:\my first mcp\weather"
uv run python server/weather.py
```

The server uses STDIO transport and waits for incoming MCP requests from compatible clients.

---

## VS Code MCP Integration

The MCP server config lives at `weather/.vscode/mcp.json`. Current working config:

```json
{
  "servers": {
    "weather": {
      "type": "stdio",
      "command": "uv",
      "args": [
        "run",
        "--project",
        ".",
        "python",
        "server/weather.py"
      ]
    }
  },
  "inputs": []
}
```

This ensures `uv` runs the script from the correct project and picks up the local environment.

---

## MCP Clients

The repository contains multiple MCP client versions developed incrementally.

Current client versions:

- client_v1.py
- client_v2.py
- client_v3.py
- client_v4.py
- client_v5.py
- client_v5_1.py

The latest version (`client_v5_1.py`) integrates:

- Gemini 2.5 Flash
- Open-Meteo Geocoding API
- Dynamic MCP Tool Selection
- Natural Language Weather Queries

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
- https://ai.google.dev
- https://open-meteo.com

---
## Detailed Documentation

Detailed implementation documentation is available in:

```text
client/README.md
server/README.md
```

These documents provide:

- Client evolution from V1 to V5.1
- Server evolution from weather.py to weather_v5_2.py
- Gemini integration
- Open-Meteo Geocoding workflow
- Open-Meteo Forecast API integration
- MCP architecture
- Learning outcomes
- Future enhancements

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

