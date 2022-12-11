#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < len(my_list) or idx > 0:
        for item in my_list:
            if item == my_list[idx]:
                return item
    else:
        return None


my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
