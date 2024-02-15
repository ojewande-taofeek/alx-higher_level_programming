#!/usr/bin/python3
"""Contains a function that adds 2 integers"""


def add_integer(a, b=98):
    """
        function that adds 2 integers
        Args:
            a: first integer
            b: second integer or 98
        Returns:
            sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
