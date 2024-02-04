#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    p_count = 0
    try:
        for x in range(x):
            print("{:d}".format(my_list[x]), end="")
            p_count += 1
    except IndexError:
        pass
    print()
    return p_count
