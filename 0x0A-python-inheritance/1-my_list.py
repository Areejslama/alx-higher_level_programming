#!/usr/bin/python3
"""fuction to print list"""


class MyList(list):
    """present subclass"""
    def print_sorted(self):
        """print list"""
        print(sorted(self))
