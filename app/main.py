from fastapi import FastAPI
from app.models import User, Trader
from .routers.trader import trader_route

app = FastAPI()

app.include_router(trader_route, prefix="/trader")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")