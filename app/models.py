from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    phone_number: int


class Trader(BaseModel):
    id: int
    company_name: str
    email: EmailStr