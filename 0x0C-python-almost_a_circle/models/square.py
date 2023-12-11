#!/usr/bin/python
"""_summary_

    Returns:
        _type_: _description_
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (class): inherit from this class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initailzer

        Args:
            size (int): size of the square
            x (int, optional): x value
            y (int, optional): y value
            id (_type_, optional): id of the square. Defaults to None.
        """
        self.__size = size
        self.width = size
        self.height = size
        super().__init__(size, size, x=0, y=0, id=None)
        self.x = x
        self.y = y

    @property
    def size(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        self.__size = self.width = self.height = value

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        len_of_args = len(args)
        if len_of_args == 0 and args is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

        if len_of_args == 1:
            self.id = args[0]
        elif len_of_args == 2:
            self.size = args[1]
        elif len_of_args == 3:
            self.id = args[2]
        elif len_of_args == 4:
            self.size = args[3]

    def to_dictionary(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
