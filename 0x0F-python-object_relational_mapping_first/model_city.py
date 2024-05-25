#!/usr/bin/python3
"""
    script for model_state.py named model_city.py that
    contains the class definition of a City
"""
from model_state import Base
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship


class City(Base):
    """
        the class definition of a City
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
    state = relationship("State", back_populates="city")
