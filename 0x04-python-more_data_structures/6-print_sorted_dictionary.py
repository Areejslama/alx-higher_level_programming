#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = {}
    new_dict = sorted(a_dictionary, key=lambda x: x)
    for i in new_dict:
        print("{}:{}".format(i, a_dictionary[i]))
