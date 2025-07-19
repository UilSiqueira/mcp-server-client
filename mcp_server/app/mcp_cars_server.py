# import uvicorn
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from app.routes.car_routes import router


app = FastAPI()
app.include_router(router)

mcp = FastApiMCP(
    app,
    name="CarService",
    description="MCP tools for car operations",
    include_operations=["cars"],
)
mcp.mount()
