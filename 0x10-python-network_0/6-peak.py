#!/usr/bin/python3
"""define a function"""


def find_peak(list_of_integers):
    """represent the function"""
    i = len(list_of_integers)
    for n in range (i):
        if (n == 0 or list_of_integers[n] >= list_of_integers[n - 1]) and ( n == i - 1 or  list_of_integers[n] >=  list_of_integers[n + 1]):
            return list_of_integers[n]
        return None

