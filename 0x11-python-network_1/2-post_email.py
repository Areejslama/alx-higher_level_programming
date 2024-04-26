#!/usr/bin/python3
"""this script to post request"""
import sys
import urllib.request
import urllib.parse
if __name__ == "__main__":
    url = sys.argv[1]
    email = urllib.parse.urlencode({'email': 'example@example.com'}.encode('UTF-8'))
    req = urllib.request.Request(url, data=email, method='POST')
    with urllib.request.urlopen(req) as response:
        html = respone.read().decode('UTF-8')
        print(html)
