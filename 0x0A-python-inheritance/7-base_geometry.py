#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be an integer")
