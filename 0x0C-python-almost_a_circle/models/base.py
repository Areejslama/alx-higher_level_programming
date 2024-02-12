#!/usr/bin/python3
"""define a base class"""

import json


class Base:
    """reprsent base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert list of dictionaries to JSON string"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list of objects to a JSON file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(list_dicts)
                file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Convert JSON string to list of dictionaries"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create instance from dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 1)
        else:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load instances from JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding='utf-8') as f:
                my_string = f.read()
                if not my_string:
                    return []
                else:
                    my_instance = cls.from_json_string(my_string)
                    return [cls.create(**obj) for obj in my_instance]
        except FileNotFoundError:
            return []
