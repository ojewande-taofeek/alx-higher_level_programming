#!/usr/bin/python3
from sys import argv
import requests
from requests.exceptions import HTTPError


if __name__ == "__main__":
    req = requests.get(argv[1])
    try:
        req.raise_for_status()
    except HTTPError:
        print(req.status_code)
    else:
        print(req.text)
