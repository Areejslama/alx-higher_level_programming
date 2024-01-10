#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return 
    sorted_keys = sorted(a_dictionary.items())
    for key, value in sorted_keys:
        print("{}: {}".format(key, value))
