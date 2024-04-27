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
    r = requests.post(url, data={'q': q})
    res = r.headers['content-type']
    if res == 'application/json':
        data = r.json()
        q_id = data.get('id')
        name = data.get('name')
        if q_id and name:
            print("[{}] {}".format(q_id, name))
        else:
            print("NO result")
    else:
        print("Not a valid JSON")
