#!/usr/bin/python3
"""this script to post request"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.post(url, data=email)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('UTF-8')
        print(html)
