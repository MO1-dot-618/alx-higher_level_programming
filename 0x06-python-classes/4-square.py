#!/usr/bin/python3
"""Square Class"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new Square"""
        self.size = size

    @property
    def size(self):
        """ getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for private instance attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns square"""
        return (self.__size ** 2)
