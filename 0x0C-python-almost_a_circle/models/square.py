#!/usr/bin/python3
"""The module for the class Square"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """A child class of class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """The class constructor"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Public instance getter for size attr"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attr"""
        self.width = value
        self.height = value

    def __str__(self):
        """The informal representation of square"""
        return "[Square] ({}) {}/{} - {}" \
               .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """update method for Square"""
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            elif i == 1:
                self.size = args[1]
            elif i == 2:
                self.x = args[2]
            elif i == 3:
                self.y = args[3]
        for key, value in kwargs.items():
            if key == "id":
                try:
                    if args[0]:
                        continue
                except IndexError:
                    self.id = value
            elif key == "size":
                try:
                    if args[1]:
                        continue
                except IndexError:
                    self.size = value
            elif key == "x":
                try:
                    if args[2]:
                        continue
                except IndexError:
                    self.x = value
            elif key == "y":
                try:
                    if args[3]:
                        continue
                except IndexError:
                    self.y = value

    def to_dictionary(self):
        """Returns a Square instance dict"""
        new_dict = dict()
        for key, value in self.__dict__.items():
            if key.endswith("width"):
                new_dict["size"] = value
            elif key.endswith("id"):
                new_dict["id"] = value
            elif key.endswith("x"):
                new_dict["x"] = value
            elif key.endswith("y"):
                new_dict["y"] = value
        return new_dict
