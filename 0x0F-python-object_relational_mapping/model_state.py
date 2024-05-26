#!/usr/bin/python3
"""
    contains the class definition of a State and an
    instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
        Inherits from Base
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    city = relationship("City", backref="cities")
