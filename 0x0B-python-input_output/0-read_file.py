#!/usr/bin/python3
"""define a function"""


def read_file(filename=""):
    """represernt the function"""
    with open("my_file_0.txt", "rt" encoding="UTF8") as my_file:
        a_file = my_file.read()
        print(a_file, end="")
