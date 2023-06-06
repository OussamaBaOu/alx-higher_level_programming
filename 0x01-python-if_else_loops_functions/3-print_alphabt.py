#!/usr/bin/python3
for a in range(97, 123):

    if a is not '4' and a is not '16':
        print("{:s}".format(chr(a)), end="")
