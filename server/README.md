# Weather MCP Server Documentation (V1 -> V5.2)

## Overview

This folder contains the MCP Weather Server implemented in `server/weather.py`. The current code uses the National Weather Service (NWS) API and exposes two tools: `get_alerts` and `get_forecast`.

This README also captures the planned V5.2 upgrade path for global weather support using Open-Meteo.

---

## Current Server (NWS-Based)

The existing server uses the National Weather Service API and is best suited for US-based locations.

### MCP Tools

#### get_forecast

Inputs:

```python
latitude: float
longitude: float
```

Returns:

* Temperature
* Wind information
* Detailed forecast
* Multi-period forecast summary

---

#### get_alerts

Input:

```python
state: str
```

Returns:

* Active alerts
* Alert severity
* Affected areas
* Instructions and descriptions

---

## V5.2 - Global Weather MCP Server (Planned)

### Overview

V5.2 upgrades the MCP server by replacing the National Weather Service (NWS) API with the Open-Meteo Weather Forecast API. This change enables worldwide weather forecasting and removes the geographical limitations of the original implementation.

---

### Why V5.2?

The original weather server used:

```text
+ National Weather Service (NWS)
```

which primarily supports weather data within the United States.

As a result:

```text
New York      yes
Chicago       yes
California    yes

Ahmedabad     no
Tokyo         no
London        no
Paris         no
```

---

### New Solution

V5.2 uses:

```text
Open-Meteo Forecast API
```

Benefits:

* Global coverage
* No API key required
* Free to use
* Fast response times
* Simple integration

---

## V5.2 Architecture

```text
User
 |
 v
Gemini 2.5 Flash
 |
 v
MCP Client (V5.1)
 |
 v
Open-Meteo Geocoding
 |
 v
Coordinates
 |
 v
Weather MCP Server (V5.2)
 |
 v
Open-Meteo Forecast API
 |
 v
Weather Data
 |
 v
Gemini Response
```

---

## V5.2 MCP Tools

### get_forecast

Inputs:

```python
latitude: float
longitude: float
```

Returns:

* Current temperature
* Humidity
* Wind speed
* 5-day forecast
* Rain probability

---

### Example Output

```text
Current Weather

Temperature:
17.4C

Humidity:
65%

Wind Speed:
8.9 km/h
```

---

### 5-Day Forecast

```text
Date: 2026-06-01
Max Temp: 23.3C
Min Temp: 14.4C
Rain Chance: 7%
```

---

## Supported Locations

The system can retrieve weather data for virtually any city worldwide.

Examples:

```text
Ahmedabad
New York
London
Tokyo
Sydney
Paris
Berlin
Dubai
Singapore
```

---

## Learning Outcomes (V5.2)

Through V5.2, the following concepts are explored:

* MCP Server Development
* External API Integration
* Global Weather Forecasting
* Open-Meteo APIs
* MCP Tool Design
* Agent + Tool Architecture
* Client-Server Communication

---

## End-to-End Workflow

```text
User Question
      |
      v
Gemini Determines Tool
      |
      v
Geocoding API
      |
      v
Coordinates
      |
      v
MCP Tool Invocation
      |
      v
Weather Forecast API
      |
      v
Weather Data
      |
      v
Gemini Explanation
      |
      v
Final Response
```

---

## Technologies Used

* Python 3.11
* MCP Python SDK
* FastMCP
* Gemini 2.5 Flash
* Google GenAI SDK
* HTTPX
* Open-Meteo Geocoding API
* Open-Meteo Forecast API
* Visual Studio Code
* GitHub Copilot

---

## Future Improvements

### V6

Multi-tool MCP agent:

* Weather tool
* Calculator tool
* Currency tool
* Time tool

### V7

Multiple MCP servers:

* Weather MCP server
* Finance MCP server
* File MCP server

with a single Gemini-powered orchestration layer.
