#!/usr/bin/python3
"""
    Python script that fetches https://alx-intranet.hbtn.io/status
    using urllib
"""
from urllib.request import Request, urlopen


if __name__ == "__main__":
    req = Request("https://alx-intranet.hbtn.io/status/")
    with urlopen(req) as the_req:
        html = the_req.read()

    utf_decode = html.decode('utf8')
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(utf_decode))
