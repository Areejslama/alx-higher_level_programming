#!/usr/bin/python3
"""define a function"""
import json


def save_to_json_file(my_obj, filename):
    """represent a function"""
    with open(filename, "w",  encoding="UTF8"):
        print(json.dumps(my_obj))
