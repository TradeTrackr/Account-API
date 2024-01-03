from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(Integer, index=True)

class Trader(Base):
    __tablename__ = 'traders'

    id = Column(String, primary_key=True, index=True)
    company_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
