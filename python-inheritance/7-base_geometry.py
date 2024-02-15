#!/usr/bin/python3
"""Module that contain the class BaseGeometry
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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be great than 0")
