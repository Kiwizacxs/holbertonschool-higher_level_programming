#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle"""


class Rectangle:
    """class that define a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize a rectangle"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = []
            for x in range(self.__height):
                for i in range(self.__width):
                    rectangle.append(str(self.print_symbol))
                if x < self.__height - 1:
                    rectangle.append("\n")
            return ("".join(rectangle))

    def __repr__(self):
        """function that return a string"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """print a menssage when the rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """method that compare two rectangles and return the bigger"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method that return a new istance of Rectagle"""
        return cls(size, size)
