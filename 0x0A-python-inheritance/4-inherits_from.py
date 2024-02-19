#!/usr/bin/python3
"""
   Write a function that returns True if the object
   is an instance of a class that inherited (directly or indirectly)
   from the specified class ; otherwise False.

    Prototype: def inherits_from(obj, a_class):
    You are not allowed to import any module
"""


def inherits_from(obj, a_class):
    """Returns as stated in the module.__doc__"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
