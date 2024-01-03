# crud.py
from sqlalchemy.orm import Session
from app import models

async def get_user_by_id(db: Session, user_id: int, company_id: str):
    return await db.get(models.User, user_id, company_id)