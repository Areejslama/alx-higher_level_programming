#!/usr/bin/python3
"""this script to post request"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    req = urllib.parse.urlencode({'email': email})
    req = req.encode('ascii')
    with urllib.request.urlopen(url, req) as response:
        html = response.read().decode('UTF-8')
        print(html)
