#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1
if number < 0:
    sign = -1
    number *= -1
i = (number % 10) * sign
number *= sign
if i > 5:
    print(f"Last digit of {number} is {i} and is greater than 5")
elif i == 0:
    print(f"Last digit of {number} is {i} and is 0")
else:
    print(f"Last digit of {number} is {i} and is less than 6 and not 0")
