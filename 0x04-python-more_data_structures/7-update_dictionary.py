#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        return
    a_dictionary.update({key: value})
    for key, value in a_dictionary.items():
        print("{}: {}".format(key, value))
