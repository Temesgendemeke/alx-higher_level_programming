#!/usr/bin/python3
"""_summary_"""

import json


def load_from_json_file(filename):
    """_summary_

    Args:
        filename (_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(filename, encoding="utf") as f:
        return json.loads(f)
        
        
        
