#!/usr/bin/python3
"""define a function to list methods"""


def lookup(obj):
    """return object"""
    return list(dir(obj))
