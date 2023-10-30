#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Represent a Rectangle """
    def __init__(self, width=0, height=0):
        """Initialize a new instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Return the perimeter of the Rectangle"""
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """Define the print() """
        strn = ""
        if self.width == 0 or self.height == 0:
            strn = strn + "\n"
        else:
            for i in range(self.height):
                for j in range(self.width):
                    strn = strn + "#"
                if i != (self.height - 1):
                    strn = strn + "\n"
        return strn
