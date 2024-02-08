#!/usr/bin/python3
def read_file(filename=""):
    with open("my_file_0.txt", encoding="UTF8") as my_file:
        a_file = my_file.read()
        print(a_file, end="")
