from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.utilities.db import get_db
from app.utilities.crud import get_trader_by_id


trader_route = APIRouter()

@trader_route.get("/get_trader/{id}", status_code=200)
async def get_trader(id: str, db: AsyncSession = Depends(get_db)) -> dict:
    trader = await get_trader_by_id(db, id)
    if trader is None:
        raise HTTPException(status_code=404, detail="Trader not found")
    return {"trader": trader}

@trader_route.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}
