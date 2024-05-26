#!/usr/bin/python3
"""
    contains the class definition of a City
"""
from model_state import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """
        maps to the cities table
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
