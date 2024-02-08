#!/usr/bin/python3
"""define json"""
import json


def to_json_string(my_obj):
    """represtentation jason

    Args:
    my_obj:object to handle
    Return:
    string represntation in json format
    """
    json_string = json.dumps(my_obj)
    return json_string
