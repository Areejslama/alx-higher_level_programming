#!/usr/bin/python3
"""represent a function"""
import json


def load_from_json_file(filename):
    """represent the function
    Args:
    filename:the name of file object
    Return:
    created object
    """
    with open(filename) as f:
        return json.load(f)
