#!/usr/bin/python3
"""The module for the class Square"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """A child class of class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """The class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The informal representation of square"""
        return "[Square]  ({}) {}/{} - {}" \
               .format(self.id, self.x, self.y, self.width)
