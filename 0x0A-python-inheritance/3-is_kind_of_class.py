#!/usr/bin/python3
"""define an object"""


def is_kind_of_class(obj, a_class):
    """represent the object"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
