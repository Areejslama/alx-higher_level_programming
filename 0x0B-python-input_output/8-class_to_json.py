#!/usr/bin/python3
"""define a function"""


def class_to_json(obj):
    """Serialize a Python object into a dictionary"""

    data = {}
    for key, value in obj.__dict__.items():
        """Serialize object"""
        if isinstance(value, (list, dict, str, int, bool)):
            data[key] = value
        else:
            """Skip serializing object"""
            pass
    return data
