#!/usr/bin/python3
for a in range(97, 123):

    if chr(a) not in ['q', 'e']:
        print("{:s}".format(chr(a)), end="")
