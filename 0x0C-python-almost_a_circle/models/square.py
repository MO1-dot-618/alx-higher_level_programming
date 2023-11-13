#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] (" + str(self.id)
        string += ") " + str(self.x) + "/" + str(self.y)
        string += " - " + str(self.height)
        return string
