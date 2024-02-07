#!/usr/bin/python3
"""define a class"""


class MyInt(int):
    def __init__(self, value):
        self.value = value

        def __eq__(self, other):
            return self.value != other.value

        def __ne__(self, other):
            return self.value == other.value
