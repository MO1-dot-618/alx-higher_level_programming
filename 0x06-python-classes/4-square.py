#!/usr/bin/python3
"""Square Class"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new Square"""
        self.size(self, size)

    def size(self):
        """ getter """
        return self.__size

    def size(self, value):
        """ Setter for private instance attribute size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns square"""
        return (self.__size ** 2)
