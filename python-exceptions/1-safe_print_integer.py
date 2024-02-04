#!/usr/bin/python3
def safe_print_integer(value):
    Error = 0
    try:
        print("{:d}".format(value))
    except ValueError:
        Error = 1
    if Error == 1:
        return False
    else:
        return True
