#!/usr/bin/python3
"""
    Write the first class Base:

    Create a folder named models with an empty file __init__.py inside
    - with this file, the folder will become a Python package

    Create a file named models/base.py:

    Class Base:
    private class attribute __nb_objects = 0
    class constructor: def __init__(self, id=None)::
    if id is not None, assign the public instance attribute id with this
    argument value - you can assume id is an integer and you don’t need
    to test the type of it
    otherwise, increment __nb_objects and assign the new value to the public
    instance attribute id
    This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes and to
    avoid duplicating the same code (by extension, same bugs)
"""
import json


class Base:
    """The base class"""
    __nb_objects = 0  # number of class instances created

    def __init__(self, id=None):
        """The class constructor
        Args:
            id(None or int): The id of an instance
        Returns:
            Nothing
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        if type(list_dictionaries) is list:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        new_list = list()
        if list_objs:
            for i in list_objs:
                list_dict = cls.to_dictionary(i)
                new_list.append(list_dict)
        elif list_objs is None:
            new_list = []
        list_dict_json = cls.to_json_string(new_list)
        filename = str(cls.__name__) + ".json"
        with open(filename, "w", encoding="utf-8") as new_file:
            new_file.write(list_dict_json)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if type(dictionary) is dict:
            if cls.__name__ == "Rectangle":
                rec = cls(3, 4)
                cls.update(rec, **dictionary)
                return rec
            elif cls.__name__ == "Square":
                squ = cls(4)
                cls.update(squ, **dictionary)
                return squ

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = str(cls.__name__) + ".json"
        instance_list = list()
        try:
            with open(filename, "r", encoding="utf-8") as new_file:
                list_dicts_str = new_file.read()
                list_dicts = cls.from_json_string(list_dicts_str)
                for each_dict in list_dicts:
                    new_instance = cls.create(**each_dict)
                    instance_list.append(new_instance)
            return instance_list
        except FileNotFoundError:
            return instance_list
