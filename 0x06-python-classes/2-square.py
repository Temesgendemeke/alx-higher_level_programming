#!/usr/bin/python3
class Square:
    """A module for square"""
    def __init__(self, size=0):
        """
        creates private attribute size
        
        checks if size is integer otherwise raises TypeError
        checks if size is greater than zero otherwise raises ValueError
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
