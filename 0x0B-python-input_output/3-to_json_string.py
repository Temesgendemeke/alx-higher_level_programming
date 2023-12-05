#!/usr/bin/python3
""" python code to json"""


import json


def to_json_string(my_obj):
    """
    >>> to_json_string([1,2,2]
    [1,2,2]
    """
    return json.dumps(my_obj)
