#!/usr/bin/python3
"""
    Write the class Rectangle that inherits from Base:

    In the file models/rectangle.py
    Class Rectangle inherits from Base
    Private instance attributes, each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
    Call the super class with id - this super call with use the logic of the
    __init__ of the Base class
    Assign each argument width, height, x and y to the right attribute
    Why private attributes with getter/setter? Why not directly public
    attribute?

    Because we want to protect attributes of our class. With a setter, you are
    able to validate what a developer is trying to assign to a variable.
    So after, in your class you can “trust” these attributes.
"""
from .base import Base


class Rectangle(Base):
    """A child class to Base
    Args:
        Base(class): The base class
    Returns:
        Nothing
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Costructor for rectangle class
            Args:
                width(int): width of the rectangle
                height(int): height of tghe rectangle
                x(int)
                y(int)
                id(int): The id of an object of the rectangle
        """
        super().__init__(id)  # calling the Base class constructor for id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """The getter for instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The getter for instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The getter for instance attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """The setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The getter for instance attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """The setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """The area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints a rectangle obj using '#'"""
        for y_column in range(self.__y):
            print()
        for row in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)
        """"print("\n".join(("#" * self.__width) \
        for row in range(self.__height)))"""

    def __str__(self):
        """Informal string representation of the class"""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
               format(self.id, self.__x, self.__y, self.__width,
                      self.__height)

    def update(self, *args, **kwargs):
        """update an object of rectangle"""
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            elif i == 1:
                self.width = args[1]
            elif i == 2:
                self.height = args[2]
            elif i == 3:
                self.x = args[3]
            elif i == 4:
                self.y = args[4]
        for key, value in kwargs.items():
            if key == "id":
                try:
                    if args[0]:
                        continue
                except IndexError:
                    self.id = value
            elif key == "width":
                try:
                    if args[1]:
                        continue
                except IndexError:
                    self.width = value

            elif key == "height":
                try:
                    if args[2]:
                        continue
                except IndexError:
                    self.height = value
            elif key == "x":
                try:
                    if args[3]:
                        continue
                except IndexError:
                    self.x = value
            elif key == "y":
                try:
                    if args[4]:
                        continue
                except IndexError:
                    self.y = value

    def to_dictionary(self):
        """Returns a Rectangle instance dict"""
        new_dict = dict()
        for key, value in self.__dict__.items():
            if key.endswith("width"):
                new_dict["width"] = value
            elif key.endswith("height"):
                new_dict["height"] = value
            elif key.endswith("id"):
                new_dict["id"] = value
            elif key.endswith("x"):
                new_dict["x"] = value
            elif key.endswith("y"):
                new_dict["y"] = value
        return new_dict
