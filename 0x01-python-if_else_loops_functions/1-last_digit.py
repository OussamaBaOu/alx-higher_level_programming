#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number >= 0:
        a = number % 10
elif number < 0:
        a = ((number * -1) % 10) * -1

if a > 5:
    str = 'Last digit of {0} is {1} and is greater than 5'
elif a < 6 and a != 0:
    str = 'Last digit of {0} is {1} and is less than 6 and not 0'
elif a == 0:
    str = 'Last digit of {0} is {1} and is 0'
print(str.format(number, last_digit))
