#!/usr/bin/python3
"""represent file"""

import json
import sys


load_file =  __import__('6-load_from_json_file').load_from_json_file
save_file =  __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"

try:
    my_file = load_file(filename)
except (FileNotFoundError, ValueError):
    my_file = []
    for args in sys.argv[1:]:
        my_file.append(args)
        save_file(my_file, filename)
