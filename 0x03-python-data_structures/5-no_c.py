#!/usr/bin/python3
def no_c(my_string):
    a = len(my_string)
    b = 0
    c = my_string[:]
    for d in range(a):
        if (my_string[d] == 'c' or my_string[d] == 'C'):
            c = c[:(d - b)] + my_string[(d + 1):]
            b += 1
        return (c)
