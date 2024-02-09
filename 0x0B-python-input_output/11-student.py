#!/usr/bin/python3
"""define a function"""


class Student:
    """reprsent a class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        data = dict()

        if type(attrs) is list and all(type(n) is str for n in attrs):
            for n in attrs:
                if n in self.__dict__:
                    data.update({n: self.__dict__[n]})
            return data
        return self.__dict__.copy()
    def reload_from_json(self, json):
        return self.__dict__.update(n: self.json[n]})
