#!/usr/bin/python3
"""Module that creates Object from json file"""

import json


def load_from_json_file(filename):
    """Creates object from json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data
