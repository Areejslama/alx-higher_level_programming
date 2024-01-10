#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return 
    dictionary = sorted(a_dictionary.items())
    for key, value in dictionary:
        print("{}:{}".format(key, value))
