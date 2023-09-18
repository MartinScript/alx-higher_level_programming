#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < len(my_list):
        new_list = [item for item in my_list]
        new_list[idx] = element
        return new_list
    else:
        return my_list


list = [1, 2, 3]
idx = 0
element = 4
new_list = new_in_list(list, idx, element)

print(new_list)
print(list)
