#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is []:
        return None
    max_v = my_list[0]
    for number in my_list:
        if number > max_v:
            max_v = number
            return max_v
