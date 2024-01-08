# crud.py
from sqlalchemy.orm import Session
from app import models


async def get_trader_by_id(db: Session, trader_id: int):
    return await db.get(models.Trader, trader_id)

async def get_user_by_id(db: Session, user_id: int, company_id: str):
    return await db.get(models.User, user_id, company_id)

async def find_account_by_email(db: Session, email: str):
    return await db.get(models.User, email)

async def get_user_by_trader_id(db: Session, company_id: str):
    return await db.get(models.User, company_id)
