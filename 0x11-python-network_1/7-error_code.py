#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request to the URL and displays
    the body of the response.
    If the HTTP status code is greater than or equal to 400, print: Error code:
    followed by the value of the HTTP status code
"""
from sys import argv
import requests
from requests.exceptions import HTTPError


if __name__ == "__main__":
    req = requests.get(argv[1])
    try:
        req.raise_for_status()
    except HTTPError:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
