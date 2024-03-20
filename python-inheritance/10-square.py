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

class Rectangle(BaseGeometry):
    """
    Clas that create a rectangle
    """
    def __init__(self, height, width):
        """
        class constructor
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
    
    def area(self):
        """Method that return the area of the trectangle"""
        return self.__height * self.__width

    def __str__(self):
        """method that return a string"""
        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):
    """Class Rectangle"""
    def __init__(self, size):
        """class constructor"""
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)
    
    def area(self):
        """return the area of the square"""
        return self.__size * self.__size
