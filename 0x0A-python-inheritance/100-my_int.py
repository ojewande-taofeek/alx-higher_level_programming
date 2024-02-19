#!/usr/bin/python3
"""
    Write a class MyInt that inherits from int:

    MyInt is a rebel. MyInt has == and != operators inverted
    You are not allowed to import any module
"""


class MyInt(int):
    """The int class rebellious child class"""
    def __init__(self, value):
        """The constructor"""
        self.__value = value

    def __eq__(self, other):
        """Magic equal method"""
        return self.__value != other

    def __ne__(self, other):
        """Magic not equal method"""
        return self.__value == other
