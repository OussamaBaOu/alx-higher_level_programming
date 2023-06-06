#!/usr/bin/python3
def uppercase(str):
    a = ""
    for c in str:
        b = ord(c)
        if b >= 97 and b <= 122:
            d = chr(b - 32)
            a += d
        else:
            a += c
            print(a)
