#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    p_count = 0
    for x in range(x):
        try:
            print("{:d}".format(my_list[x]), end="")
            p_count += 1
        except (ValueError, TypeError):
            pass
    print()
    return p_count
