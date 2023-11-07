#!/usr/bin/python3
"""Module that appends to a file"""


def append_write(filename="", text=""):
    """appends to file and return num of chars"""
    with open(filename, 'a', encoding="utf-8") as f:
        data = f.write(text)
    return data
