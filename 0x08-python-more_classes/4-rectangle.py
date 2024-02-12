#!/usr/bin/python3
"""The module defines class Rectangle based on 3-rectangle.py"""


class Rectangle:
    """Class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """The getter for width"""
        return self.__width

    @property
    def height(self):
        """The getter for height"""
        return self.__height

    @width.setter
    def width(self, value):
        """The setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """The setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """print() and str() should print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for h in range(self.__height))

    def __repr__(self):
        """return a string representation of the rectangle to be
           able to recreate a new instance by using eval()
        """
        return ("{}({},{})".format(self.__class__.__name__,
                self.__width, self.__height))
