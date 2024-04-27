#!/usr/bin/python3
"""this script to handle json"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        q = sys.argv[1]
    else:
        q = ""
    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data={'q': q})
    if response.headers.get('content-type') == 'application/json':
        data = response.json()
        if data:
            _id = data.get('id')
            name = data.get('name')
            if _id and name:
                print("[{}] {}".format(_id, name))
            else:
                print("No result")
        else:
            print("No result")
    else:
        print("Not a valid JSON")
