#!/usr/bin/python3
"""
function that returns a set of all elements present in only one set
"""


def only_diff_elements(set_1, set_2):
    """convert sets into list"""
    new_set_1 = [x for x in set_1]
    new_set_2 = [x for x in set_2]
    """add list"""
    new_set = new_set_1 + new_set_2
    for item in new_set:
        """if item in both set"""
        if item in new_set_1 and item in new_set_2:
            """remove item"""
            new_set.remove(item)
    return new_set
