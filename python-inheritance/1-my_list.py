#!/usr/bin/python3
"""module that contain the class MyList"""


class MyList(list):
    """class that contain a function"""

    def print_sorted(self):
        """fnction that print a sorted list"""
        print(sorted(self))
