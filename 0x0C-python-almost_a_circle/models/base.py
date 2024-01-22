#!/usr/bin/python3
""" base """

import json

class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """fun to init information"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """fun"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """fun"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            json.write("[]")
        else:
            list_dicts = [o.to_dictionary() for o in list_objs]
            json.write(Base.to_json_string(list_dicts))
