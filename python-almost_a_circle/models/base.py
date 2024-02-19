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

    @static.method
    def to_json_string(list_dictionaries):
        """
        Static method that return a dictionary in JSON format
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dump(list_dictionaries)
