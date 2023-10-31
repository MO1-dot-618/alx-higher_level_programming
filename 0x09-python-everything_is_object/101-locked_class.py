#!/usr/bin/python3
"""Module for class prevents the user from dynamically creating instances"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """ Initalizing meth """
        pass
