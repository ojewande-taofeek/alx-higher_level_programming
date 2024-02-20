#!/usr/bin/python3
"""
    Write a script that adds all arguments to a Python list,
    and then save them to a file:

    You must use your function save_to_json_file from
    5-save_to_json_file.py
    You must use your function load_from_json_file from
    6-load_from_json_file.py
    The list must be saved as a JSON representation
    in a file named add_item.json
    If the file doesn’t exist, it should be created
    You don’t need to manage file permissions / exceptions.
"""
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

new_list = []
try:
    new_list = load_from_json_file("add_item.json")
except Exception:
    pass
for i in range(1, len(sys.argv)):
    new_list.append(sys.argv[i])
save_to_json_file(new_list, "add_item.json")
