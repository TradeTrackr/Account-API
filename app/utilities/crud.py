# crud.py
from nis import cat
from sqlalchemy.orm import Session
from app import models
from sqlalchemy import select


async def get_trader_pub(db: Session, trader_id: str):
    query = select(models.Trader.company_url, 
                   models.Trader.company_name, 
                   models.Trader.email, 
                   models.Trader.company_response_email, 
                   models.Trader.company_logo_url).where(models.Trader.id == trader_id)
    result = await db.execute(query)
    
    # Fetching the first result if available
    trader = result.scalars().first()

    return trader

async def get_trader_by_url(db: Session, url: str):
    result = await db.execute(select(models.Trader).where(models.Trader.company_url == url))
    return result.scalars().first()

async def get_trader_by_id(db: Session, trader_id: str):
    return await db.get(models.Trader, trader_id)

async def get_user_by_id(db: Session, user_id: int, company_id: str):
    return await db.get(models.User, user_id, company_id)

async def find_account_by_email(db: Session, email: str):
    result = await db.execute(select(models.User).where(models.User.email == email))
    return result.scalars().all()

async def get_user_by_trader_id(db: Session, company_id: str):
    result = await db.execute(select(models.User).where(models.User.trader_id == company_id))
    return result.scalars().all()

async def get_categories_for_trader(db: Session, id: str):
    result = await db.execute(select(models.Category).where(models.Category.trader_id == id))
    return result.scalars().all()


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
