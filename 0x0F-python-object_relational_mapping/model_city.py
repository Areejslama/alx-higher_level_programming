#!/usr/bin/python3
"""this script to define city"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, column, String

Base = declarative_base()

class city(Base):
    """city class to represent table"""
    __tablename__ = 'cities'
    id = column(Integer, Primary_key= True)
    name = column(String(128), nullable=False)
    state_id = column(Integer, Forign_key=True)
