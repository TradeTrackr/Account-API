from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone_number: int


class Trader(BaseModel):
    id: str
    company_name: str
    email: EmailStr