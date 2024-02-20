#!/usr/bin/python3
"""
    Write a class Student that defines a student by:

    Public instance attributes:
    first_name
    last_name
    age
    Instantiation with first_name, last_name and age:
    def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None): that retrieves a
    dictionary representation of a Student instance
    (same as 8-class_to_json.py)
    If attrs is a list of strings, only attribute names
    contained in this list must be retrieved.
    Otherwise, all attributes must be retrieved
    You are not allowed to import any module
    You are not allowed to import any module
"""


class Student:
    """a class Student that defines a student based 9-students.py"""
    def __init__(self, first_name, last_name, age):
        """Instantiation method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        new_dict = dict()
        for attr in attrs:
            for key, value in self.__dict__.items():
                if attr == key:
                    new_dict[key] = value
        return new_dict
