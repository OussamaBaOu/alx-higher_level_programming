#!/usr/bin/python3
"""
   this function finds peak in list
"""


def find_peak(numbr):
    '''
        Finds peak in list of numbers
    '''
    length = len(numbr)
    if length == 0:
        return None
    if length == 1:
        return (numbr[0])
    if length == 2:
        return numbr[0] if numbr[0] >= numbr[1] else numbr[1]

    for a in range(0, length):
        value = numbr[a]
        if (a > 0 and a < length - 1 and
                numbr[a + 1] <= value and numbr[a - 1] <= value):
                return value
        elif a == 0 and numbr[a + 1] <= value:
            return value
        elif a == length - 1 and numbr[a - 1] <= value:
            return value
    return pick
