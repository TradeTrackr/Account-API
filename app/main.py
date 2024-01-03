from fastapi import FastAPI
from app.models import User, Trader
from app.routers.trader import trader_route

app = FastAPI()

app.include_router(trader_route)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")