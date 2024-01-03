from fastapi import APIRouter

trader_route = APIRouter()

@trader_route.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}
