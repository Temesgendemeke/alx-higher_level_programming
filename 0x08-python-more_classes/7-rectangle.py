#!/usr/bin/python3
"""documention for module"""


class Rectangle:
    """_summary_

    Raises:
        TypeError: _description_
        ValueError: _description_
        TypeError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """_summary_

        Args:
            width (int, optional): _description_. Defaults to 0.
            height (int, optional): _description_. Defaults to 0.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        string representation of the rectangle by
        concatenating rows of '#' characters.

        Returns:
            str: "#" in respect reactangular shape
        """
        if self.width == 0 or self.width == 0:
            return ""
        rectangle_str = ''
        s = ""
        if isinstance(self.print_symbol, list):
            for i in range(self.height):
                s += f"['{self.print_symbol[0]}', '{self.print_symbol[1]}', '{self.print_symbol[2]}']" * self.width
            return s
      
        for _ in range(self.height):
            rectangle_str += self.print_symbol * self.width + '\n'
        return rectangle_str

    def __repr__(self) -> str:
        """_summary_

        Returns:
            str: returns represention
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """_summary_

        Returns:
            str : when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def area(self):
        """returns areas of reactangle"""
        return self.height * self.width

    def perimeter(self):
        """returns perimeter of reactangle"""
        if self.width == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)
