#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for value in my_list:
        if value in my_list and value not in new_list:
            new_list.append(value)
            sum += value
    return sum
