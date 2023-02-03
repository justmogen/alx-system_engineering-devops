#!/usr/bin/python3

"""addition function"""


def add_integer(a, b=98):
    """adding integer a and b

    Check if a and b are ints before addition
    Raises:
    TypeError: if one of a or b is non-integer or float
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
