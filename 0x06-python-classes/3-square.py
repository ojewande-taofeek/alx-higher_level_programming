#!/usr/bin/python3
"""A module that defines defines a square by: (based on 2-square.py) """


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """The initialization method
            Args:
                size: The size of a sqaure
            Return:
                Nothing
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the current square area"""
        return (self.__size ** 2)
