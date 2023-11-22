#!/usr/bin/python3
"""_summary_
    """


class Square:
    def __init__(self, size=0):
        """
        initialize an instance

        Args:
            size (int, optional):  assign size to self.size
        """
        self.size = size

    @property
    def size(self):
        """
        getter

        Returns:
            int: readly only size
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
        Returns:
            int: current square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        prints in stdout the square with the character #:
         if size is zero prints nothing
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
