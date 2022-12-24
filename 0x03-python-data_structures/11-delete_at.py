#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    my_list = [x for x in my_list if x != my_list[idx]]
    return my_list
