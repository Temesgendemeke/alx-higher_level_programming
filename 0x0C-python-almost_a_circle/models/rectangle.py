#!/usr/bin/python3
"""_summary_"""

import json
class Base:
    """_summary_"""
    __nb_objects = 0

    def __init__(self, id=None):
        """_summary_

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
           list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
            file.write(json_str)
        


class Rectangle(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """_summary_

        Args:
            width (_type_): _description_
            height (_type_): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        super().__init__(self.id)

    @property
    def width(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__width

    @width.setter
    def width(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        "getter"
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def id(self):
        """getter"""
        return self.__id

    @id.setter
    def id(self, value):
        """setter"""
        self.__id = value

    def area(self):
        """return area of the rectangle"""
        return (self.__height * self.__width)
    def display(self):
        """print '#' respect to height and width"""
        for y in range(self.__y):
            print()
        for i in range(self.__height):
                print(" " * self.__x + "#" * self.__width)
    def __str__(self) -> str:
        return f"[Rectangle] ({self.__id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    def update(self, *args, **kwargs):
        num_args = len(args)
        
        if (args is None or num_args == 0) and  kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.__id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value
        if num_args >= 1:
            self.__id = args[0]
        if num_args >= 2:
            self.__width = args[1]
        if num_args >= 3:
            self.__height = args[2]
        if num_args >= 4:
            self.__x = args[3]
        if num_args >= 5:
            self.__y = args[4]
    def to_dictionary(self):
        return {'x': self.__x, 'y': self.__y , 'id': self.__id, 'height': self.__height, 'width': self.__width}
       
                