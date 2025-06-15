from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="math")

@mcp.tool
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool
def subtract(a: int, b: int) -> int:
    return a - b

# transport = "stdio" argument tells the server to :
# Use standard input and output for communication to send and receive and respood to tool function calls 

if __name__ == "__main__":
    mcp.run(transport="stdio")