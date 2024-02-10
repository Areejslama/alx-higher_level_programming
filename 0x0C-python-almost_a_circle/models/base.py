#!/usr/bin/python3
"""define a base class"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """represent base class"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
