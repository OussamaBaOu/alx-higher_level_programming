#!/usr/bin/python3
"""Module to find max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return max integer in list of integers
        If the list is empty, function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    a = 1
    while a < len(list):
        if list[a] > result:
            result = list[a]
        a += 1
    return result
