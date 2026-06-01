# MCP Weather Client Documentation (V1 -> V5.1)

## Project Overview

This project demonstrates the evolution of an MCP (Model Context Protocol) Client that communicates with a Weather MCP Server.

The goal was not only to learn how to call MCP tools, but also to understand how modern AI agents interact with MCP servers.

The Weather MCP Server exposes two tools:

```python
get_forecast(latitude, longitude)

get_alerts(state)
```

The MCP Client gradually evolved from a simple tool discovery client into an intent-driven assistant capable of automatically selecting tools based on user requests. V5 adds a Gemini 2.5 Flash powered agent that chooses tools and reasons over tool output. V5.1 adds global geocoding so the client can resolve cities worldwide at runtime.

---

# Architecture

```text
User
 |
 v
MCP Client
 |
 v
MCP Protocol (STDIO)
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

## Tech Stack (Client Focus)

* Python 3.11
* MCP Python SDK
* FastMCP
* HTTPX
* Gemini 2.5 Flash
* Google GenAI SDK
* Visual Studio Code
* GitHub Copilot

# V1 - Tool Discovery Client

## Objective

Learn how an MCP Client connects to an MCP Server and discovers available tools.

---

## Workflow

```text
Client
 |
 v
Connect to Server
 |
 v
Initialize Session
 |
 v
List Available Tools
```

---

## What Happens Internally

### Step 1

Create a connection using:

```python
stdio_client()
```

This launches the MCP server as a subprocess.

---

### Step 2

Create an MCP session.

```python
ClientSession()
```

The session manages communication between the client and server.

---

### Step 3

Initialize the connection.

```python
await session.initialize()
```

This performs the MCP handshake.

---

### Step 4

Request available tools.

```python
await session.list_tools()
```

---

## Example

Input:

```text
Run Client
```

Output:

```text
Available Tools:

- get_alerts
- get_forecast
```

---

## Concepts Learned

* MCP Client
* MCP Server
* Session Initialization
* Tool Discovery
* STDIO Transport

---

# V2 - Tool Inspection Client

## Objective

Learn how AI agents inspect tool metadata before calling tools.

---

## Why This Matters

Modern AI agents do not blindly call tools.

They first inspect:

```text
Tool Name
Description
Input Schema
```

to understand:

```text
What does the tool do?
What inputs are required?
When should it be used?
```

---

## Workflow

```text
List Tools
 |
 v
Inspect Tool Metadata
 |
 v
Display Schema
```

---

## Example

Tool:

```python
get_forecast(
    latitude,
    longitude
)
```

Client Output:

```text
Tool Name: get_forecast

Description:
Get weather forecast for a location.

Input Schema:
{
  latitude: number,
  longitude: number
}
```

---

## Concepts Learned

* Tool Metadata
* Tool Descriptions
* Tool Schemas
* MCP Introspection

---

# V3 - Command-Based MCP Client

## Objective

Allow users to execute tools using predefined commands.

---

## Problem With V2

The client could inspect tools but could not actually use them interactively.

---

## Solution

Create a command-driven interface.

---

## Workflow

```text
User Command
 |
 v
Client Parser
 |
 v
Tool Selection
 |
 v
MCP Tool Call
```

---

## Supported Commands

### List Tools

```text
tools
```

---

### Show Details

```text
details
```

---

### Forecast

```text
forecast 40.7128 -74.0060
```

---

### Alerts

```text
alerts NY
```

---

## Example

User:

```text
forecast 40.7128 -74.0060
```

Client:

```python
await session.call_tool(
    "get_forecast",
    {
        "latitude": 40.7128,
        "longitude": -74.0060
    }
)
```

Server:

```python
get_forecast()
```

Response:

```text
Today:
Temperature: 74F
Forecast: Sunny...
```

---

## Concepts Learned

* Tool Invocation
* User Input Handling
* Dynamic Parameters
* Interactive CLI Applications

---

# V4 - Intent-Based MCP Client

## Objective

Make the client behave more like an AI assistant.

---

## Problem With V3

Users must remember exact commands.

Example:

```text
forecast 40.7128 -74.0060
```

This is not natural.

---

## Solution

Introduce Intent Detection.

The client interprets the request and automatically chooses the correct MCP tool.

---

## Workflow

```text
User Request
 |
 v
Intent Detection
 |
 v
Select Tool
 |
 v
Call MCP Tool
 |
 v
Display Result
```

---

# Intent Detection

The client uses pattern matching and regular expressions.

Example:

```python
re.search(...)
```

---

## Forecast Detection

User:

```text
weather 40.7128 -74.0060
```

Client Detects:

```text
Intent:
Forecast
```

Client Calls:

```python
get_forecast()
```

---

## Alerts Detection

User:

```text
alerts for NY
```

Client Detects:

```text
Intent:
Alerts
```

Client Calls:

```python
get_alerts()
```

---

## Tool Listing Detection

User:

```text
list tools
```

Client Detects:

```text
Intent:
Tool Listing
```

Client Calls:

```python
session.list_tools()
```

---

## Tool Details Detection

User:

```text
show tool details
```

Client Detects:

```text
Intent:
Tool Inspection
```

Client Calls:

```python
show_tool_details()
```

---

# Example Conversation

User:

```text
weather 40.7128 -74.0060
```

Client:

```text
Fetching Forecast...
```

Server:

```python
get_forecast()
```

Response:

```text
Temperature: 74F
Wind: 6 mph
Forecast: Sunny
```

---

# V5 - Gemini-Powered MCP Agent

## Objective

Replace rule-based intent detection with Gemini 2.5 Flash. The model automatically decides which MCP tool to use, when to use it, and how to interpret the result.

---

# V5 Architecture

```text
User
 |
 v
Gemini 2.5 Flash
 |
 v
Tool Selection
 |
 v
MCP Client
 |
 v
Weather MCP Server
 |
 v
Weather API
 |
 v
Gemini Reasoning
 |
 v
Final Response
```

---

# Example Queries

```text
What's the weather in New York?

Should I carry an umbrella tomorrow in Chicago?

Any alerts for NY?

Do I need a jacket in Los Angeles?
```

---

# Example Gemini Tool Decision

```json
{
    "tool": "get_alerts",
    "state": "NY"
}
```

---

# Example Agent Response

```text
There is a Special Weather Statement for parts of New York.

Dense fog may reduce visibility to a quarter mile.

Drive carefully if traveling in affected areas.
```

---

# Concepts Learned in V5

* LLM Tool Selection
* MCP + Gemini Integration
* AI Agent Foundations
* Tool Reasoning
* Structured Outputs
* Function Calling Concepts

---

# V5.1 - Gemini-Powered MCP Client with Global Geocoding

## Overview

V5.1 upgrades the MCP client from a static city-based implementation to a dynamic AI-powered client capable of handling weather requests for cities worldwide.

The client uses:

* Gemini 2.5 Flash for tool selection
* Open-Meteo Geocoding API for city-to-coordinate conversion
* MCP protocol for tool communication
* Weather MCP Server for weather retrieval

Unlike previous versions that relied on hardcoded city mappings, V5.1 dynamically resolves locations at runtime.

---

## Architecture

```text
User
 |
 v
Gemini 2.5 Flash
 |
 v
Tool Selection
 |
 v
Open-Meteo Geocoding API
 |
 v
Latitude / Longitude
 |
 v
MCP Client
 |
 v
Weather MCP Server
```

---

## Key Features

### AI-Based Tool Selection

Gemini analyzes natural language queries and automatically selects the appropriate MCP tool.

Example:

```text
Should I carry an umbrella tomorrow in Tokyo?
```

Gemini Output:

```json
{
    "tool": "get_forecast",
    "city": "Tokyo"
}
```

---

### Global City Support

Supports weather requests for cities worldwide.

Examples:

```text
Weather in Ahmedabad

Forecast for London

Should I carry an umbrella in Tokyo?

Weather in Sydney
```

---

### Dynamic Geocoding

Instead of maintaining hardcoded coordinates, the client uses Open-Meteo Geocoding API:

```text
City Name
            |
            v
Geocoding API
            |
            v
Latitude / Longitude
```

Example:

```text
Ahmedabad
|
v
23.02579, 72.58727
```

---

## Example Execution

User:

```text
What's the weather in New York?
```

Gemini:

```json
{
    "tool": "get_forecast",
    "city": "New York"
}
```

Geocoding:

```text
New York
|
v
40.71427, -74.00597
```

MCP Tool:

```python
get_forecast(
        latitude=40.71427,
        longitude=-74.00597
)
```

---

## Learning Outcomes (V5.1)

* MCP Client Development
* Gemini Tool Calling
* LLM-Based Routing
* Geocoding APIs
* Structured JSON Responses
* Agent Foundations
* Tool Orchestration

---

# Evolution Summary

## V1

```text
Connect
List Tools
```

Learned:

* MCP Basics
* Tool Discovery

---

## V2

```text
Inspect Tools
Read Schemas
```

Learned:

* Tool Metadata
* MCP Introspection

---

## V3

```text
User Commands
Tool Invocation
```

Learned:

* Calling MCP Tools
* Interactive Clients

---

## V4

```text
Intent Detection
Automatic Tool Selection
```

Learned:

* Agent-Like Behaviour
* Intent Routing
* Tool Selection Logic

---

## V5

```text
Gemini Tool Selection
Automatic Tool Use
```

Learned:

* LLM Tool Selection
* AI Agent Foundations
* Tool Reasoning

---

## V5.1

```text
Global Geocoding
Dynamic City Resolution
```

Learned:

* Geocoding APIs
* LLM-Based Routing
* Tool Orchestration

---

# Real-World Connection

Modern AI frameworks follow a similar pattern.

Examples:

```text
LangGraph
CrewAI
AutoGen
OpenAI Agents SDK
Claude MCP
Gemini Tool Calling
```

Architecture:

```text
User
 |
 v
LLM
 |
 v
Tool Selection
 |
 v
MCP Client
 |
 v
MCP Server
 |
 v
External System
```

The V4 client is essentially a simplified version of this architecture without using an LLM.

The V5 client extends this with Gemini-driven tool selection and response synthesis. V5.1 adds global geocoding so the client can route requests for cities worldwide.

---

# Future Versions (V6+)

---

## V6

Multi-Server MCP Client

```text
Client
 |-- Weather MCP
 |-- Calculator MCP
 |-- File Reader MCP
 |-- Database MCP
```

---

## V7

Agentic MCP System

```text
User
 |
 v
LLM Agent
 |
 v
Planner
 |
 v
Multiple MCP Servers
 |
 v
Final Response
```

---

# Key Learning Outcomes

Through V1-V5.1, the following MCP concepts were implemented:

* MCP Client Development
* MCP Server Communication
* STDIO Transport
* Session Management
* Tool Discovery
* Tool Introspection
* Tool Invocation
* Intent Detection
* Automatic Tool Selection
* Agent Foundations
* LLM Tool Selection
* MCP + Gemini Integration
* Tool Reasoning
* Structured Outputs
* Function Calling Concepts
* Geocoding APIs
* LLM-Based Routing
* Tool Orchestration

These concepts form the foundation of modern MCP-powered AI systems and agent architectures.
