#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """_summary_

        Raises:
            Exception: _description_
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """_summary_

        Args:
            name (_type_): _description_
            value (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be an integer".format(name))
