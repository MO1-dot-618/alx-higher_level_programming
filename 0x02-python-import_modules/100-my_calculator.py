#!/usr/bin/python3
if __name__ != "__main__":
    exit()
operators = ['+', '-', '*', '/']
from calculator_1 import add, sub, mul, div
functions = [add, sub, mul, div]

import sys
if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
if sys.argv[2] not in operators:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

a, b = sys.argv[1], sys.argv[3]
for op in range (len(operators)):
    if sys.argv[2] == operators[op]:
        print("{} {} {} = {}".format(a, operators[op], b, functions[op](int(a), int(b))))
