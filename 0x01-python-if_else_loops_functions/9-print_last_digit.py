#!/usr/bin/python3
def print_last_digit(number):
    sign = 1
    if number < 0:
        sign = -1
        number *= -1
    i = (number % 10) * sign
    print(f"{i:d}")
    return i
