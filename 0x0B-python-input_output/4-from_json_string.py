#!/usr/bin/python3
"""Module for JSON representation"""

import json


def from_json_string(my_str):
    """Represents JSON obecjt"""
    return json.loads(my_str)
