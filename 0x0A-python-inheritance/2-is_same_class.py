#!/usr/bin/python3
"""define subclass"""


def is_same_class(obj, a_class):
    """represent the subclass"""
    if issubclass(a_class, int):
        return True
    else:
        return False
