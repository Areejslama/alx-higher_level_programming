#!/usr/bin/python3
"""represent file"""

import json
import sys
save_file = __import__('5-save_to_json_file').save_to_json_file
load_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    data = load_file(filename)
except (FileNotFoundError, ValueError):
    data = []

for arg in sys.argv[1:]:
    data.append(arg)

save_file(data, filename)
