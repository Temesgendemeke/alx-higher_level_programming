#!/usr/bin/python3
"""json to object"""

import json


def from_json_string(my_str):
    """
    >>> from_json_string(true)
    True
    """
    return json.loads(my_str)
