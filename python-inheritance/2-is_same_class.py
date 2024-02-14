#!/usr/bin/python3
"""module that contain a the
function is_same_class
"""


def is_same_class(obj, a_class):
    """function that check if an object
    blongs to a class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
