#!/usr/bin/python3
""" child of list class"""


class MyList(list):
    """class"""

    def print_sorted(self):
        print(sorted(self))
