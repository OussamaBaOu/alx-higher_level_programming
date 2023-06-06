#!/usr/bin/python3
def uppercase(str):
    a = list(str)
    for b in range(len(a)):
        if (ord(a[b]) > 96 and ord(a[b]) < 123):
            a[b] = chr(ord(a[b]) - 32)
    print("{}".format("".join(a)))
