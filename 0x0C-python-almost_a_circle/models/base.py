#!/usr/bin/python3
"""define a base class"""
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """represent base class"""
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

            def to_json_string(list_dictionaries):
                if list_dictionaries is None:
                    return "[]"
                else:
                    return json.dumps(list_dictionaries)

                @classmethod
                def save_to_file(cls, list_objs):
                    filename = cls.__name__ + ".json"
                    with open(filename, mode='w') as file:
                        if list_objs is None:
                            file.write("[]")
                        else:
                            for obj in list_objs:
                                list_dicts = [obj.to_dictionary()]
                                json_string = cls.to_json_string(list_dicts)
                                file.write(json_string)

                            def from_json_string(json_string):
                                if json_string is None:
                                    return "[]"
                                else:
                                    return json.loads(json_string)

                                @classmethod
                                def create(cls, **dictionary):
                                    if cls.__name__ == "Rectangle":
                                        dummy = cls(1, 1, 1)
                                        dummy.update(**dictionary)
                                        return dummy
