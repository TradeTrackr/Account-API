from fastapi import FastAPI
from app.models import User, Trader
from .routers.trader import trader_route
from .routers.user import user_route
from .routers.auth import auth_route
from .routers.category import category_route

app = FastAPI()

app.include_router(trader_route, prefix="/trader")
app.include_router(user_route, prefix="/user")
app.include_router(auth_route, prefix="/auth")
app.include_router(category_route, prefix="/category")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")