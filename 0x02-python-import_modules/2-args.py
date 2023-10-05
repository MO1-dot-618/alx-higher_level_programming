#!/usr/bin/python3
import sys
if __name__ != '__main__':
    sys.exit()

lol = len(sys.argv) - 1
index = 1
if lol == 1:
    print("1 argument:")
elif lol == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(lol))

for i in sys.argv[1:]:
    print("{}: {}".format(index, i))
    index += 1
