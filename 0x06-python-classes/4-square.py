#!/usr/bin/python3
"""A module for square"""


class Square:
    """_summary_
    """
    def __init__(self, size=0):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """_summary_

        Returns:
            _type_: _description_
        """
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
