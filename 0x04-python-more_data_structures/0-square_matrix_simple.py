#!/usr/bin/python

def square_matrix_simple(matrix=[]):
    square_matrix = list(
        map(lambda row: list(map(lambda x: x * x, row)), matrix))
    return square_matrix


matrix = [[]]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
