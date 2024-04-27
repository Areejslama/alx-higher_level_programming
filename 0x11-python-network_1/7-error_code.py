#!/usr/bin/python3
"""this script to handle error"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    try:
        r =  requests.get(url)
        r.raise_for_status()
        pass
    except requests.RequestException as e:
        print("Error code:", e)
