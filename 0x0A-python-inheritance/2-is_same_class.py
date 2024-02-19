#!/usr/bin/python3
"""
    Write a function that returns True if the object is
    exactly an instance of the specified class ; otherwise False.

    Prototype: def is_same_class(obj, a_class):
    You are not allowed to import any module
"""


def is_same_class(obj, a_class):
    """
        function that returns True if the object is exactly an
        instance of the specified class ; otherwise False
        Args:
            obj: an instance of a class
            a_class: Any class
    """
    if type(obj) is a_class:
        return True
    return False
