#!/usr/bin/python3
""" Function that look up available attributes and
    methods of an object"""


def lookup(obj):
    """

    Args:
        obj (object): object to be checked

    Returns:
        list: returns the list of available attributes
        and methods of an object:
    """
    return dir(obj)
