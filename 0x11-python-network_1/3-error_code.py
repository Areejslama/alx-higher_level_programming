#!/usr/bin/python3
"""this script to handle error"""
import sys
import urllib.request
if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req) as response:
            html = response.read().decode('UTF-8')
            print(html)
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
