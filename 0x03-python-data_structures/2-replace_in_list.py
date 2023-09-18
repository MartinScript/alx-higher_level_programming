#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return my_list
    for i, item in enumerate(my_list):
        if idx == i:
            my_list[i] = element
    return my_list


list = [0]
idx = 0
element = 4
new_list = replace_in_list(list, idx, element)

print(new_list)
print(list)
