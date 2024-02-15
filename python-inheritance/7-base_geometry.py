#!/usr/bin/python3
"""Module that contain the class BaseGeometry
with all his functions
"""


class BaseGeometry:
    """Class BaseGeometry that contain the methods:
    area() and integer_validator()
    """
    def area(self):
        """function that are not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that valides that value is
        an integer
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be great than 0".format(name))
