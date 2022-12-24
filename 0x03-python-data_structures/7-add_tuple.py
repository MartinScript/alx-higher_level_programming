#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = tuple(map(lambda x, y: x + y, tuple_a, tuple_b))
    return new_tuple
