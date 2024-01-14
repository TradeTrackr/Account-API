import imp
from unicodedata import category
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.utilities.db import get_db
from app.utilities.crud import get_category_for_trader, new_catagory
from app.utilities.authentication import Authentication
from app.validation_models import Category

category_route = APIRouter()

# get trader by id
@category_route.get("/get_categories/{id}", status_code=200)
async def get_trader(id: str, user=Depends(Authentication.validate_token), db: AsyncSession = Depends(get_db)) -> dict:
    categories = await get_category_for_trader(db, id)
    if categories is None:
        raise HTTPException(status_code=404, detail="No categories found")
    return {"categories": categories}

@category_route.post("/new_category")
async def new_category(category: Category, db: AsyncSession = Depends(get_db)) -> dict:
    
    new_category = await new_catagory(db, category)

    return {"message": "Category created successfully.", "id": new_category.id}
