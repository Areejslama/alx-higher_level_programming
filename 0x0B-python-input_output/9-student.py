#!/usr/bin/python3
"""define a class"""


class Student:
    """reprsent a class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def to_json(self):
        data = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (str, int, dict)):
                data[key] = value
            else:
                pass
        return data
