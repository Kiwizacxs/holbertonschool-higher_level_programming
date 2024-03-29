#!/usr/bin/python3
"""
Module that contain the class Square
that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square that create a square whit all
    his methods
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initialice square using super()
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        get the value of size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        set value for size
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        str function that return a string
        with the attributes
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} -\
 {self.width}"

    def update(self, *args, **kwargs):
        """
        Public method that assigns attributes:

        *args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        attr = ["id", "size", "x", "y"]
        if args:
            for x in range(len(args)):
                if x < len(attr):
                    setattr(self, attr[x], args[x])
            if len(args) >= 4:
                setattr(self, "y", args[3])
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Public method that return a dictionary with the attributes
        """
        return {
                "id": self.id,
                "x": self.x,
                "size": self.width,
                "y": self.y
                }
