#!/usr/bin/python3
def uppercase(str):
    a = ""
    for b in range(len(str)):
        if (ord(str[b]) >= 97 and ord(str[b]) <= 122):
            a += chr(ord(str[b]) - 32)
            continue
        a += str[b]

        print('{0}'.format(a))
