#!/usr/bin/python3
"""
    Write a function that returns True if the object
    is an instance of, or if the object is an instance of
    a class that inherited from, the specified class ; otherwise False.

    Prototype: def is_kind_of_class(obj, a_class):
    You are not allowed to import any module
"""


def is_kind_of_class(obj, a_class):
    """
        function that returns True if the object is an instance of
        of a class or its parent; otherwise returns false
        Args:
            obj: An object
            a_class: A class
        Returns:
            True, if isinstance
            False, if otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
