import imp
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.utilities.db import get_db
from app.utilities.crud import get_trader_by_id
from app.validation_models import TokenData
from app.utilities.authentication import Authentication

auth_route = APIRouter()

# get trader by id
@auth_route.get("/check_token", status_code=200)
async def get_trader(token_data: TokenData) -> dict:
    return {"valid_token": Authentication().validate_token_bool(token_data.access_token)}
