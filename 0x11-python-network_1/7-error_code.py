#!/usr/bin/python3
"""this script to handle error"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
        r =  requests.get(url)
        text = 'Error code: {}'
        code = r.status_code
        if (code >= 400):
            print(text.format(code))
        else:
            print(r.text)
