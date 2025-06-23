from mcp.server.fastmcp import FastMCP


mcp=FastMCP("Weather")

@mcp.tool()
def get_weather(city: str) -> str:
    """Returns the current weather for a given city."""
    # Placeholder implementation
    return f"The current weather in {city} is sunny."


if __name__ == "__main__":
    mcp.run(transport="streamable_http")