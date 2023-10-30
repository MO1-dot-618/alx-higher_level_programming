#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Represent a Rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new instance"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                    strn = strn + str(self.print_symbol)
                if i != (self.height - 1):
                    strn = strn + "\n"
        return strn

    def __repr__(self):
        """Return the string representation of the Rectangle """
        rect = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return (rect)

    def __del__(self):
        """Print a message after deletion of instance"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """compare triangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
