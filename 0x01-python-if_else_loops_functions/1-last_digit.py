#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = abs(number) % 10
if number < 0:

    a = -a
    print("Last digit of {} is {} and is ".format(number, a), end="")

if number > 5:

    print("Last digit of {} is {} and is greater than 5".format(number, a), end="")

elif number == 0:

    print("Last digit of {} is {} and is 0".format(number, a), end="")

else:

    print("less than 6 and not 0")
