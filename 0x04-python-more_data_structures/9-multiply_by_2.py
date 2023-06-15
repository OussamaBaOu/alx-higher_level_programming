#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = a_dictionary.copy()
    b = list(a.keys())
    for c in b:
        a[c] *= 2
    return (a)
