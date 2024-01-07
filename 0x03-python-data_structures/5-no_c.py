#!/usr/bin/env python3
def no_c(my_string):
    removed_chars = ['c', 'C']
    new_string = ""
    for char in my_string:
        if char not in removed_chars:
            new_string += char
    return new_string
