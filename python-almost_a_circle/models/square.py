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

    def __str__(self):
        """
        str function that return a string
        with the attributes
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} -\
 {self.width}"
