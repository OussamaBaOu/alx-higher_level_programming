#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = abs(number) % 10
if number < 0:

    a = -a
    print("Last digit of {} is {} and is ".format(number, a), end="")

if a > 5:

    print("Last digit of {} is {} and isgreater than 5".format(number, a))

elif a == 0:

    print("Last digit of {} is {} and is0".format(number, a))

else:

    print("less than 6 and not 0")
