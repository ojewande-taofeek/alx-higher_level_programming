#!/usr/bin/python3
"""
    Write a function that writes an Object to a text file,
    using a JSON representation:

    Prototype: def save_to_json_file(my_obj, filename):
    You must use the with statement
    You don’t need to manage exceptions if the object can’t be serialized.
    You don’t need to manage file permission exceptions.
"""
import json


def save_to_json_file(my_obj, filename):
    """
        function that writes an Object to a text file,
        using a JSON representation
        Args:
            my_obj(object): A Python object
            filename(str): A file name
        Returns:
            Nothing
    """
    with open(filename, "a", encoding="utf-8") as new_file:
        json.dump(my_obj, new_file)
