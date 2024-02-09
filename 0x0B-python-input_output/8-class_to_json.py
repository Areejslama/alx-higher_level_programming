#!/usr/bin/python3
"""define a function"""


def class_to_json(obj):
    """represent a function"""
    data = {}
    for key, value in obj._dict_.items():
        """serialize object"""
        if is instance(value, (list, dict, str, int, bool):
                data[key] = value
        else:
        """skip serializing object"""
        pass

        return data
