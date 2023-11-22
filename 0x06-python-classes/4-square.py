#!/usr/bin/python3
"""doc for module"""


class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """
       Setter

       Args:
           size (size): size to be squared

       Raises:
           TypeError: if its not integer
           ValueError: if size is less than zero
       """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Getter

        Returns:
           return the values
        """
        return self.__size * self.__size
