#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8).
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    try:
        req = Request(argv[1])
        with urlopen(req) as the_req:
            html = the_req.read()
        print(html.decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
