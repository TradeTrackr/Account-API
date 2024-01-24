import imp
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.utilities.db import get_db
from app.utilities.crud import get_trader_by_id
from app.utilities.authentication import Authentication
from app.validation_models import TraderModel

trader_route = APIRouter()

# get trader by id
@trader_route.get("/get_trader/{id}")
async def get_trader(id: str, user=Depends(Authentication().validate_token), db: AsyncSession = Depends(get_db)) -> dict:
    trader = await get_trader_by_id(db, id)
    if trader is None:
        raise HTTPException(status_code=404, detail="Trader not found")
    return {"trader": trader}

# get trader bool for ui enquiry post
@trader_route.get("/check_trader/{id}", response_model=TraderModel)
async def check_trader(id: str, db: AsyncSession = Depends(get_db)) -> dict:
    trader = await get_trader_by_id(db, id)
    if trader is None:
        return False

    return TraderModel(
        id=trader.id,
        company_name=trader.company_name,
        email=trader.email,
        company_url=trader.company_url,
        company_logo_url=trader.company_logo_url,
        company_response_email=trader.company_response_email
    )
