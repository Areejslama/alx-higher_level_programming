#!/usr/bin/python3
"""define a function"""


def append_write(filename="", text=""):
    """represent the function"""
    with open(filename, "a", encoding="UTF8") as f:
        return (f.write(text))
