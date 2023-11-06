#!/usr/bin/python3
""" function to return methods"""


def inherits_from(obj, a_class):
    """ type """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
