#!/usr/bin/python3
def magic_calculation(a, b):
    d = 0
    for c in range(1, 3):
        try:
            if c > a:
                raise Exception('Too far')
            else:
                d += a ** b / c
        except:
            d = b + a
            break
    return (d)
