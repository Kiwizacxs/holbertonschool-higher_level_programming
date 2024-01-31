#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = []
    if idx > len(my_list) - 1 or idx < 0:
        return my_list
    else:
        i = 0
        while i != len(my_list):
            new_list.append(my_list[i])
            i += 1
        new_list[idx] = element
        return new_list
