#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = my_list[:]
    for c, b in enumerate(my_list):
        if b % 2 == 0:
            a[c] = True
        else:
            a[c] = False
    return(a)
