#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle"""


class Rectangle:
    """class that define a rectangle"""
    def __init__(self, width=0, height=0):
        """initialize a rectangle"""
        self.width = width
        self.height = height

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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """return the area of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """str method that return a string"""
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        else:
            for x in range(self.__height):
                for i in range(self.__width):
                    rectangle.append("#")
            if x < self.__height - 1:
                rectangle.append("\n")
            return rectangle

    def __repr__(self):
        """function that return a string"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
