#!/usr/bin/python3
class Square:
    """A module for square"""
    def __init__(self, size=0):
        """
        checks if size is integer otherwise raises TypeError
        checks if size is greater than zero otherwise raises ValueError
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
