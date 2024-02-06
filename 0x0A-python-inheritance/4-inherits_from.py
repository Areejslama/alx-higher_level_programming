#!/usr/bin/python3
"""define a sub class"""


def inherits_from(obj, a_class):
    """return true object is an instance of a class that inherited"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
