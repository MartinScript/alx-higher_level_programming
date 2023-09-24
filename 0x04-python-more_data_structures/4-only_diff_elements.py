#!/usr/bin/python3
"""
function that returns a set of all elements present in only one set
"""


def only_diff_elements(set_1, set_2):
    """convert sets into list"""
    new_set_1 = [x for x in set_1]
    new_set_2 = [x for x in set_2]
    """add list"""
    new_set = set(new_set_1 + new_set_2)
    return new_set


set_1 = {"Python"}
set_2 = {"Python"}
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
