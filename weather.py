from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="weather")

@mcp.tool()
def get_weather(city: str) -> str:
    return f"The weather in Tokyo is sunny."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")