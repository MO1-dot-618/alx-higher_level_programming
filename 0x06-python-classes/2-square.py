#!/usr/bin/python3
"""task 0"""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
