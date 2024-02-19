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
        attr = ["id", "size", "x", "y"]
        if args:
            if len(args) < len(attr):
                for x in range(len(args)):
                    setattr(self, attr[x], args[x])
            if len(args) >= 4:
                setattr(self, "y", args[3])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
