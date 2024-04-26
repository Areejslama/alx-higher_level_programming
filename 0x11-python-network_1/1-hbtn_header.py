#!/usr/bin/python3
"""this script to send request to header"""
import sys
import urllib.request
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        html = (response.headers["X-Request-Id"])
        print(html)
