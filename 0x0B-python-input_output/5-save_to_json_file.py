#!/usr/bin/python3
"""Module that write Object to text file"""

import json


def save_to_json_file(my_obj, filename):
    """Writes JSON object to text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        data = json.dump(my_obj, f)
    return data
