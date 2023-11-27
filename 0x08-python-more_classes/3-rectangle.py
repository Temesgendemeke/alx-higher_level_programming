#!/usr/bin/python3
"""documention for module"""


class Rectangle:
    """_summary_
    """
    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height attribute setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """width attribute getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width attribute setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def __str__(self) -> str:
        """
        string representation of the rectangle by
        concatenating rows of '#' characters.

        Returns:
            str: "#" in respect reactangular shape
        """
        if self.width == 0 or self.width == 0:
            return ""
        rectangle_str = ''
        for _ in range(self.height):
            rectangle_str += '#' * self.width + '\n'
        return rectangle_str

    def area(self):
        """returns areas of reactangle"""
        return self.height * self.width

    def perimeter(self):
        """returns perimeter of reactangle"""
        if self.width == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)
