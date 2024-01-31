#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    n = 0
    while n != len(matrix):
        i = 0
        while i != len(matrix[n]):
            print("{:d}".format(matrix[n][i]), end="")
            if i < len(matrix[i]) - 1:
                print(" ", end="")
            i += 1
        print()
        n += 1
