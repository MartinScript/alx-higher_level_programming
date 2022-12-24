#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < len(my_list) or idx > 0:
        for item in my_list:
            if item == my_list[idx]:
                my_list[idx] = element
                return my_list
    else:
        return my_list
