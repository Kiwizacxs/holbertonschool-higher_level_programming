#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle"""


class Rectangle:
    """class that define a rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get width attr"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width attr"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get height attr"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height attr"""
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
