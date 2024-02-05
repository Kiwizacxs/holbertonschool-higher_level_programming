#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """square class"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize size"""
        self.__size = size
        self.__position = position

    def area(self):
        """return area of the square"""
        return self.__size * self.__size

    @property
    def position(self):
        """get position"""
        return self.position

    @position.setter
    def position(self, value):
        """set position of a square"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = value

    @property
    def size(self):
        """get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size of a square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """print an square"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                if self.__position[1] > 0:
                    print()
            for x in range(self.__size):
                print(" " * self.__position[0], end="")
                for i in range(self.__size):
                    print("#", end="")
                print()
