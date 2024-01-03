from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.utilities.db import get_db
from app.utilities.crud import get_user_by_id, get_user_by_company_id


user_route = APIRouter()

@user_route.get("/get_user/{id}/{company_id}", status_code=200)
async def get_user(id: int, company_id: str, db: AsyncSession = Depends(get_db)) -> dict:
    user = await get_user_by_id(db, id, company_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}

@user_route.get("/get_users_for_trader/{company_id}", status_code=200)
async def get_user(id: str, db: AsyncSession = Depends(get_db)) -> dict:
    user = await get_user_by_company_id(db, id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}
