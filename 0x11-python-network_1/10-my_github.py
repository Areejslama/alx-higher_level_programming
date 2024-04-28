#!/usr/bin/python3
"""this script to handle auth"""
import sys
import requests
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    auth = (username, password)
    r =  requests.get(url, auth=auth)
    if r.status_code == 200:
        print(r.text)
    else:
        print("check your credentials")
