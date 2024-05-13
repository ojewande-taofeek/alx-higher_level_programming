#!/usr/bin/python3
"""
    Python script that fetches https://alx-intranet.hbtn.io/status
    You must use the package requests
"""
import requests


if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    # utf_dec = req.decode('utf8')
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
