#!/usr/bin/python3
class Square:
    """
Square Module

This module defines the Square class, which represents a square
with a specified side length. It includes a method to obtain a
dictionary representation of the square.

Example:
    mysquare = Square(3)
    print(mysquare.dict_())  # Output: {'side': 3}
"""
    
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
