#!/usr/bin/python3
"""Contains a function that prints a square with the character #"""


def print_square(size):
    """
        function that prints a square with the character #
        Args:
            size: size length of the square (int)
        Returns:
            Nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size <= 0:
        raise TypeError("size must be an integer")
    for n in range(size):
        print("#" * size)
