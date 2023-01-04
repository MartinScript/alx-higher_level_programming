#!/usr/bin/python3
"""
a function that returns a set of common elements in two sets
"""


def common_elements(set_1, set_2):
    new_set = []
    for item in set_1:
        """if item in both set"""
        if item in set_1 and item in set_2:
            """add to a new set"""
            new_set.append(item)
    return new_set
