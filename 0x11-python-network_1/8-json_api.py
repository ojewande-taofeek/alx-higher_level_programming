#!/usr/bin/python3
"""
    Python script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
from sys import argv
import requests


if __name__ == "__main__":
    q = ""
    if len(argv) > 1:
        if not argv[1].isdigit():
            q = argv[1]
    payload = {'q': q}
    try:
        req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
        new_json = req.json()
        if new_json.get("id"):
            print("[{}] {}".format(new_json.get("id"), new_json.get("name")))
        elif not new_json.get("id"):
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
