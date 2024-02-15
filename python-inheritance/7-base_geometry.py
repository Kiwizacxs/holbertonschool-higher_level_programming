#!/usr/bin/python3
"""
Module that contain the class BaseGeometry
with all his methods and functions for now.
"""


class BaseGeometry:
    """
    Class BaseGeometry

    Contain the methods:
    - area()
    - integer_validator()
    """
    def area(self):
        """
        function that are not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that valides that value is
        an integer
        raise an Error if value is not int and
        raise an Error if value is less or equal 0
        Name aways are a string.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
