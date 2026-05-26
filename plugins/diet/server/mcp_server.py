# /// script
# dependencies = ["mcp[cli]", "httpx"]
# ///

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import fitbit
import withings
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("diet")


@mcp.tool()
def get_fitbit_data(date: str) -> dict:
    """Fetch FitBit activity and sleep data for a given date (YYYY-MM-DD).
    Returns steps, calories burned, activity minutes, sleep minutes, and weight if logged."""
    return fitbit.fetch(date)


@mcp.tool()
def get_withings_data(date: str) -> dict:
    """Fetch Withings scale and sleep data for a given date (YYYY-MM-DD).
    Returns weight, BMI, body composition (fat/muscle/water/bone), and sleep breakdown."""
    return withings.fetch(date)


mcp.run()
