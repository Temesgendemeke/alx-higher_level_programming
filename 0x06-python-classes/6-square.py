#!/usr/bin/python3
"""_summary_
    """


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
        initialize an instance

        Args:
            size (int, optional):  assign size to self.size
        """
        self.size = size
        self.position = position
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
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")  
        self.__position = value
    def area(self):
        return self.__position ** 2
    def my_print(self):
        if self.__size== 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                for z in range(self.__position[1]):
                    for x in range(self.__position[0]):
                        print("_", end="")
                print("#", end="")
            print()
            
            
            
            