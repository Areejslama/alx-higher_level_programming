#!/usr/bin/python3
"""represent file"""
import json
import sys

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

try:
    new = load(file)
except (FileNotFoundError, ValueError):
    new = []
    for i in sys.argv[1:]:
        new.append(i)
        save(new, file)
