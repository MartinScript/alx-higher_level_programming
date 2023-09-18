#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    for i in range(2):
        new_tuple[i] = tuple_a[i] + tuple_b[i]
    return tuple(new_tuple)
