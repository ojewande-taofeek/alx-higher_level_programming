#!/usr/bin/python3
"""A module that defines defines a square by: (based on 5-square.py) """


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """The initialization method
            Args:
                size: The size of a sqaure
            Return:
                Nothing
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """To retrieve size attribute"""
        return self.__size

    @property
    def position(self):
        """To retrieve position attribute"""
        return self.__position

    @position.setter
    def position(self, value):
        """To set position attribute"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for d in range(self.position[1]):
                print()
            for a in range(self.size):
                for c in range(self.position[0]):
                    print(" ", end="")
                for b in range(self.size):
                    print("#", end="")
                print()
