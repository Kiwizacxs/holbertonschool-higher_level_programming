#!/usr/bin/python3
"""
Module that contain the class
Rectangle that inherits rom base
with all his functions
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
        """
        Method that initialice the rectangle
        """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be > 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """
        Method to get the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        Method to print the rectangle using a determinate
        character
        """
        print("\n" * self.__y, end="")
        for x in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        str function that return a string
        with the attributes
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -\
 {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        that assigns an argument to each attribute:

        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """
        attr = ["id", "width", "height", "x", "y"]
        if args:
            for x in range(len(args)):
                setattr(self, attr[x], args[x])
            if len(args) >= 5:
                setattr(self, "y", args[4])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Public method that return a dictionary with the attributes
        """
        return {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "heigth": self.height,
                "width": self.width
                }
