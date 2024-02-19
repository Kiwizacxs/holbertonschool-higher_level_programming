#!/usr/bin/python3
"""
Module that contai the class Base whit the class
contructor and more
"""
import json


class Base:
    """
    class Base that contain an privatte atributte and
    the class constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialize the atrr
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that return a dictionary in JSON format
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        method that writes the JSON string
        in a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                _dict = []
                for obj in list_objs:
                    _dict.append(obj.to_dictionary())
                f.write(Base.to_json_string(_dict))


