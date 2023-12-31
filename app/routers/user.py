from fastapi import APIRouter, HTTPException, Depends
import jwt
from app import config
from app.utilities.crud import get_user_by_id, get_user_by_trader_id, find_account_by_email
from app.utilities.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

user_route = APIRouter()

@user_route.get("/validate-email")
def validate_email(email: str):
    # Logic to check if email exists in accounts
    # For example:
    account = find_account_by_email(email)
    if account:
        return {"status": "ok"}
    else:
        raise HTTPException(status_code=404, detail="Email not found")

@user_route.get("/get_user/{id}/{company_id}", status_code=200)
async def get_user(id: int, company_id: str, db: AsyncSession = Depends(get_db)) -> dict:
    user = await get_user_by_id(db, id, company_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}

@user_route.get("/get_users_for_trader/{company_id}", status_code=200)
async def get_user(id: str, db: AsyncSession = Depends(get_db)) -> dict:
    user = await get_user_by_trader_id(db, id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}
