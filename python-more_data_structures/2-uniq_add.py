#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_list = []
    x = 0
    while x != len(my_list) - 1:
        if x not in sum_list:
            sum_list.append(x)
        x += 1
    add = sum(sum_list)
    return add
