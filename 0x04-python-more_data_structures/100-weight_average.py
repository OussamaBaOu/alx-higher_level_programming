#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    a = 0
    b = 0
    for c in my_list:
        a += c[0] * c[1]
        b += c[1]
    return (a / b)
