#!/usr/bin/python3
"""
Module that contai the class Base whit the class
contructor and more
"""


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
