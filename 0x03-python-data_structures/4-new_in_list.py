#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        i = my_list.copy()
        if idx < 0:
            return i
        if idx >= len(my_list):
            return i
        i[idx] = element
        return i
    return my_list
