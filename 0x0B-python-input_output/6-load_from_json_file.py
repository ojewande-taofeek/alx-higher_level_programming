#!/usr/bin/python3
"""
    Write a function that creates an Object from a “JSON file”:

    Prototype: def load_from_json_file(filename):
    You must use the with statement
    You don’t need to manage exceptions if the JSON string
    doesn’t represent an object.
    You don’t need to manage file permissions / exceptions.
"""
import json


def load_from_json_file(filename):
    """
        function that creates an Object from a “JSON file”
        Args:
            filename(str): The file name
        Returns:
            Nothing
    """
    with open(filename, "r", encoding="utf-8") as new_file:
        return json.load(new_file)
