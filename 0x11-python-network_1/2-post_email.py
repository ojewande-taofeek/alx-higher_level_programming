#!/usr/bin/python3
"""
    Python script that takes in a URL and an email, sends a POST request to the
    passed URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8)
"""
from urllib.request import Request, urlopen
from sys import argv
import urllib.parse


if __name__ == "__main__":
    val = dict()
    val["email"] = argv[2]
    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    req = Request(argv[1], data)
    with urlopen(req) as the_req:
        html = the_req.read()
    print(html.decode('utf-8'))
