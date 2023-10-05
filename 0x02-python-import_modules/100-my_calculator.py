#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ != "__main__":
    exit()
op = ['+', '-', '*', '/']
fn = [add, sub, mul, div]

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
if sys.argv[2] not in op:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

a, b = sys.argv[1], sys.argv[3]
for o in range(len(op)):
    if sys.argv[2] == op[o]:
        print("{} {} {} = {}".format(a, op[o], b, fn[o](int(a), int(b))))
        break
