#!/usr/bin/python3
"""this script to handle error"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    r =  requests.get(url)
    print(r.raise_for_status())
