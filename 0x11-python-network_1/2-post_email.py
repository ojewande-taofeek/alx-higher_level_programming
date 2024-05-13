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
    data = urllib.parse.urlencode(argv[2])
    data = data.encode('ascii')
    req = Request(argv[1], data)
    with urlopen(req) as the_req:
        html = the_req.read()
    utf8_dec = html.decode('utf-8')
    print("Your email is: {}".format(utf8_dec))
