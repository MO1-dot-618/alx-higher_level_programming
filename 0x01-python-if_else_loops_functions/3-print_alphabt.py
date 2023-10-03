#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if i not in (101, 113):
        print("{}".format(chr(i)), end='')
