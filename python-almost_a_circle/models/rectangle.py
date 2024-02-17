#!/usr/bin/python3
"""
Module that contain the class
Rectangle with all his functions
"""


from .base import Base


class Rectangle(Base):
    """class rectangle with the private attributes:
        __width -> width
        __height -> height
        __x -> x
        __y -> y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Get the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle
        """
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle
        """
        self.__height = value

    @property
    def x(self):
        """
        Get the get of the rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x of the rectangle
        """
        self.__x = value

    @property
    def y(self):
        """
        Get the y of the rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y of the rectangle
        """
        self.__y = y
