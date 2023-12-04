#!/usr/bin/python3
"""_summary_"""


def is_same_class(obj, a_class):
    """_summary_

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_

    Returns:
        bool: true otherwise false
    """
    if type(obj) is a_class:
        return True
    return False
