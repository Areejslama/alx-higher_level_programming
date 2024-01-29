#!/usr/bin/python3
''' define a function to add name '''


def say_my_name(first_name, last_name=""):
    ''' represent the function

    Args:
    first_name: the first name
    last_name: the last name

    Raises:
    TypeError: if first_name or last_name not a string

    Return:
    full name or void

    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
