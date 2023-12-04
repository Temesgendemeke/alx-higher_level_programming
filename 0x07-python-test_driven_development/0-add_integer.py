#!/usr/bin/python3
"""_summary_"""
def add_integer(a, b=98):
    """
    >>> x.add_integer(3,2)
    5
    >>> x.add_integer(2)
    100
    >>> x.add_integer(76,99)
    175
    >>> x.add_integer(-99)
    -1
    >>> x.add_integer(6,0)
    6
    >>>
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
if __name__ == 'main':
    import doctest
    doctest.testmod()
    