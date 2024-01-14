# crud.py
from nis import cat
from sqlalchemy.orm import Session
from app import models


async def get_trader_by_id(db: Session, trader_id: int):
    return await db.get(models.Trader, trader_id)

async def get_user_by_id(db: Session, user_id: int, company_id: str):
    return await db.get(models.User, user_id, company_id)

async def find_account_by_email(db: Session, email: str):
    return await db.get(models.User).fiter(models.User.email==email).all()

async def get_user_by_trader_id(db: Session, company_id: str):
    return await db.get(models.User).fiter(models.User.trader_id==company_id).all()

async def get_category_for_trader(db: Session, id: str):
    return await db.get(models.Category).fiter(models.Category.trader_id==id).all()

async def new_catagory(db: Session, category):
    db_user = db.Category(
                            category=category.category,
                            colour=category.colour,
                            trader_id=category.trader_id
                        )
    
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
