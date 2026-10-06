from fastmcp import FastMCP
import random
import json

mcp = FastMCP('Simple Calculator Server')

@mcp.tool
def add(a:int,b:int)->int:
    """Adds two integers
       Args:
           a: first int
           b: second int
        Returns:
           the sum of a and b
    """
    return a + b
@mcp.tool
def random_number(min_val:int=1,max_val:int=100):
    """generates a random integer
       Args:
           min_val: minimum value
           max_val: maximum value
        Returns:
           a random integer
    """
    return random.randint(min_val,max_val)

@mcp.resource("info://server")
def server_info()-> str:
    "get information about this server."
    info = {
        "name":"simple calculator sever",
        "version": "1.0.0",
        "description": "A basic mcp server with tools",
        "tools":["add",'random_number'],
        "author":"quarmul"
    }
    return json.dumps(info,indent=2)
if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)