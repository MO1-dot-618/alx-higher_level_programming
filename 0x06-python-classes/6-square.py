#!/usr/bin/python3
"""Square Class"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """ getter """
        return self.__size

    @property
    def position(self):
        """ getter for position"""
        return self.__position

    @size.setter
    def size(self, value):
        """ Setter for private instance attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """ setter for position"""
        if (not isinstance(value[0], int) or not isinstance(value[1], int)
                or len(value) != 2 or not isinstance(value, tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints square to stdout """
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for z in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print("")
