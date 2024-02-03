#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_list = []
    x = 0
    for x in my_list:
        if x not in sum_list:
            sum_list.append(x)
    add = sum(sum_list)
    return add
