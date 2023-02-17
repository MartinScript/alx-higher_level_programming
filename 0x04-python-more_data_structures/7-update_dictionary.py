#!/usr/bin/python3
"""
function that replaces or adds key/value in a dictionary
"""


def update_dictionary(a_dictionary, key, value):
    """create a new dictionary with the key value pair"""
    new_dict = {key: value}
    """update the dictionary"""
    a_dictionary.update(new_dict)
    return a_dictionary
