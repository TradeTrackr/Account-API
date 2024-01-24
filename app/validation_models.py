from pydantic import BaseModel, EmailStr
from typing import Optional


class User(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone_number: int


class Trader(BaseModel):
    id: str
    company_name: str
    email: EmailStr


class TokenData(BaseModel):
    access_token: str


class Category(BaseModel):
    id: int
    category: str
    colour: str
    trader_id: str


class TraderModel(BaseModel):
    id: Optional[str] = None
    company_name: str
    email: str
    company_url: str
    company_logo_url: str
    company_response_email: str

    class Config:
        orm_mode = True
