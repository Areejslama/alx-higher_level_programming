#!/usr/bin/python3
"""define a function"""


def write_file(filename="", text=""):
    """represent the function"""
    with open(filename, 'w', encoding="UTF8") as f:
        return f.write(text)
