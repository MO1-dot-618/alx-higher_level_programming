#!/usr/bin/python3
import sys
if __name__ != '__main__':
    sys.exit()
sum = 0
for i in sys.argv[1:]:
    sum += int(i)
print(sum)
