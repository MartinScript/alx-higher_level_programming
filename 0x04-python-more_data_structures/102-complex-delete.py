#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    new_dict = {k: v for k, v in a_dictionary.items() if v != value}
    return new_dict


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary):
        print(key + ":", a_dictionary[key])


a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, "C")
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
