#!/usr/bin/python3
class Square:
    """
    Square Module
    This module defines the Square class, which represents a square
    with a specified side length. It includes a method to obtain a
    dictionary representation of the square.
    """
    def __init__(self, size=0):
        """
        Initialize the Square with a given size.

        Args:
            size (int): size to be squared

        Raises:
            TypeError: if size is not intger
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
