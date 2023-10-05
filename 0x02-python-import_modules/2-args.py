#!/usr/bin/python3
import sys
if __name__ != '__main__':
    sys.exit()

l = len(sys.argv) - 1
index = 1
if l == 1:
    print("{} argument:".format(l))
elif l == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(l))

for i in sys.argv[1:]:
    print("{}: {}".format(index, i))
    index += 1
