#!/usr/bin/python3
"""define a function"""


def read_file(filename=""):
    """represernt the function"""

    with open(filename, encoding="UTF8") as my_file:
        a_file = my_file.read()
        print(a_file, end="")
