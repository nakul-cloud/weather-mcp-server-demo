from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("weather")


OPEN_METEO_API = (
    "https://api.open-meteo.com/v1/forecast"
)


# ----------------------------------
# Helper Function
# ----------------------------------

async def make_request(
    url: str,
    params: dict[str, Any]
):

    async with httpx.AsyncClient() as client:

        try:

            response = await client.get(
                url,
                params=params,
                timeout=30.0
            )

            response.raise_for_status()

            return response.json()

        except Exception as e:

            print(
                f"API ERROR: {e}"
            )

            return None


# ----------------------------------
# Forecast Tool
# ----------------------------------

@mcp.tool()
async def get_forecast(
    latitude: float,
    longitude: float
) -> str:
    """
    Get weather forecast for any location
    worldwide.

    Args:
        latitude: latitude
        longitude: longitude
    """

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "wind_speed_10m"
        ],
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_probability_max"
        ],
        "forecast_days": 5
    }

    data = await make_request(
        OPEN_METEO_API,
        params
    )

    if not data:

        return (
            "Unable to fetch weather data."
        )

    current = data["current"]

    daily = data["daily"]

    output = []

    output.append(
        f"""
Current Weather

Temperature:
{current['temperature_2m']}°C

Humidity:
{current['relative_humidity_2m']}%

Wind Speed:
{current['wind_speed_10m']} km/h
"""
    )

    dates = daily["time"]

    max_temps = (
        daily["temperature_2m_max"]
    )

    min_temps = (
        daily["temperature_2m_min"]
    )

    rain_probs = (
        daily[
            "precipitation_probability_max"
        ]
    )

    output.append(
        "\n5-Day Forecast\n"
    )

    for i in range(
        len(dates)
    ):

        output.append(
            f"""
Date: {dates[i]}
Max Temp: {max_temps[i]}°C
Min Temp: {min_temps[i]}°C
Rain Chance: {rain_probs[i]}%
"""
        )

    return "\n".join(output)


# ----------------------------------
# Alerts Tool
# ----------------------------------

@mcp.tool()
async def get_alerts(
    state: str
) -> str:
    """
    Placeholder weather alerts tool.

    Open-Meteo does not provide
    NWS-style alerts.

    Args:
        state: state code
    """

    return (
        "Weather alerts are currently "
        "supported only in the original "
        "NWS server version."
    )


# ----------------------------------
# Run Server
# ----------------------------------

def main():

    mcp.run(
        transport="stdio"
    )


if __name__ == "__main__":

    main()