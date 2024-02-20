#!/usr/bin/python3
import json
"""
    Write a function that returns the JSON
    representation of an object (string):

    Prototype: def to_json_string(my_obj):
    You don’t need to manage exceptions if the object can’t be serialized.
"""


def to_json_string(my_obj):
    """
        function that returns the JSON representation of an object (string)
        Args:
            my_obj(object): Any python object
        Returns:
            string representation of my_obj
    """
    return json.dumps(my_obj)
