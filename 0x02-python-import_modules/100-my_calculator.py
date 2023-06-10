#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if (__name__ == "__main__"):
    argc = len(argv)
    d = 0
    e = ["+", "-", "*", "/"]
    if (argc != 4):
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    if (argv[2] not in e):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    c = argv[2]
    b = int(argv[3])
    if (c == "+"):
        d = add(a, b)
    elif (c == "-"):
        d = sub(a, b)
    elif (c == "*"):
        d = mul(a, b)
    else:
        d = div(a, b)
    print("{} {} {} = {}".format(a, c, b, d))
