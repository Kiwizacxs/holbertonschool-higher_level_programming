#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = 0
    new_matrix = []
    while x != len(matrix):
        new_matrix.append(list(map(lambda x: x * x, matrix[x])))
        x += 1
    return new_matrix