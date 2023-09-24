#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for a in matrix:
            for b in a:
                print("{:d}".format(b), end=" ")
            print("")
