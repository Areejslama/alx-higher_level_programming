#!/usr/bin/python3
"""this script to post request"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    e = {"email:", email)
    r = requests.post(url, data=e)
    print(r.text)
