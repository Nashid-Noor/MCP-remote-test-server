from fastmcp import FastMCP
import random
import json

mcp= FastMCP("Test remote server")

@mcp.tool()
def add(a:int, b:int) -> int:
    return a+b
@mcp.tool()
def generate_random_number(min:int, max:int) -> int:
    return random.randint(min, max)

@mcp.resource("info://resource")
def get_info() -> dict:
    return json.dumps({"name": "Test remote server", 
    "version": "1.0.0", 
    "description": "A test remote server with basic tools",
    "tools": ["add", "generate_random_number"],
    })

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000) 