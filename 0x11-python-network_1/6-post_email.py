#!/usr/bin/python3
"""this script to post request"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = ({'email': 'email'})
    r = requests.post(url, data=email)
    print(r.text)
