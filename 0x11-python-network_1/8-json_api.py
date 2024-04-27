#!/usr/bin/python3
"""this script to handle json"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1] if len(sys.argv) >= 2 else ""}
    r = requests.post(url, data)
    res = r.headers['content-type']
    if res == 'application/json':
        result = r.json()
        q_id = result.get('id')
        name = result.get('name')
        if q_id and name:
            print("[{}] {}".format(q_id, name))
        else:
            print("NO result")
    else:
        print("Not a valid JSON")
