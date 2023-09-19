#!/usr/bin/python3
"""
function that returns a set of all elements present in only one set
"""


def only_diff_elements(set_1, set_2):
    new_set = set_1 - set_2
    return new_set


set_1 = {"Python", "Javascript"}
set_2 = {"Python", "Javascript"}
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))
