from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Trader(Base):
    __tablename__ = 'traders'

    id = Column(String, primary_key=True, index=True)
    company_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    company_url = Column(String, index=True)
    company_logo_url = Column(String, index=True)
    company_response_email = Column(String, index=True)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String, index=True)
    trader_id = Column(String, ForeignKey('traders.id'))
    user_type = Column(String, index=True)


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    colour = Column(String, unique=True, index=True)
    trader_id = Column(String, ForeignKey('traders.id'))
