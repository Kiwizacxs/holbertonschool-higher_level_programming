#!/usr/bin/python3
"""
module that contain a the
function is_same_class
"""


def inherits_from(obj, a_class):
    """Function that returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
