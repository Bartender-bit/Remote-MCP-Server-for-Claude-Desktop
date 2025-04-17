from typing import Any, Dict
import httpx
from mcp.server.fastmcp import FastMCP

# 初始化FastMCP服务器
# port随便填，别与其他应用冲突就行
mcp = FastMCP(
    name="weather",
    host="127.0.0.1",
    port=8000,
    description="simple add function",
    sse_path='/sse'
)



@mcp.tool()
def add(a: int, b: int) -> int:
    """Add remote two numbers"""
    return a + b


if __name__ == "__main__":
    # init and start server
    try:
        print("Starting server...")
        mcp.run(transport='sse')
    except Exception as e:
        print(f"Error: {e}")