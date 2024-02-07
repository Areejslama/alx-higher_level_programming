#!/usr/bin/python3
"""define a class"""


class MyInt(int):
    """represent the subclass"""
    def __eq__(self, other):
        return int(self) != other

    def __ne__(self, other):
        return int(self) == other
