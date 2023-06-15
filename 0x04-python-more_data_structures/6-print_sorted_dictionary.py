#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = list(a_dictionary.keys())
    a.sort()
    for b in a:
        print("{}: {}".format(b, a_dictionary.get(b)))
