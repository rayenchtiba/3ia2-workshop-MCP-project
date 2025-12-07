from mcp.server.fastmcp import FastMCP
mcp= FastMCP(
    name="multi_tool_server",
)

@mcp.tool()
def add(a: float, b: float) -> str:
    """Additionne deux nombres"""
    from calculator import add as add_func
    return add_func(a, b)

@mcp.tool()
def subtraction(a: float, b: float) -> str:
    """Soustrait deux nombres"""
    from calculator import subtraction
    return subtraction(a, b)

@mcp.tool()
def multiply(a: float, b: float) -> str:
    """Multiplie deux nombres"""
    from calculator import multiply
    return multiply(a, b)

@mcp.tool()
def divide(a: float, b: float) -> str:
    """Divise deux nombres"""
    from calculator import divide
    return divide(a, b)
@mcp.tool()
def say_hello(name):
    return f"Hello from chtibaa to {name}!"




if __name__ == "__main__":
    mcp.run(transport='stdio')
