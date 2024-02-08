#!/usr/bin/python3
import json
"""define jason representation"""


def to_json_string(my_obj):
    """represtentation jason"""
    json_string = json.dumps(my_obj)
    return json_string
