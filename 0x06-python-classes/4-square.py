#!/usr/bin/python3
"""A module that defines defines a square by: (based on 3-square.py) """


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """The initialization method
            Args:
                size: The size of a sqaure
            Return:
                Nothing
        """
        self.size = size

    @property
    def size(self):
        """To retrieve size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """To set size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the current square area"""
        return (self.__size ** 2)
