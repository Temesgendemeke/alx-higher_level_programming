#!/usr/bin/python3
"""_summary_"""


def is_kind_of_class(obj, a_class):
    """_summary_

    Args:
        obj (_type_): _description_
        a_class (_type_): _description_

    Returns:
        bool: true or false
    """
    if isinstance(obj, a_class):
        return True
    return False
