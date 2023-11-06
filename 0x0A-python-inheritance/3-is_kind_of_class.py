#!/usr/bin/python3
""" function to return methods"""


def is_kind_of_class(obj, a_class):
    """ type """

    if type(obj) == a_class or issubclass(type(obj), a_class):
        return True
    return False
