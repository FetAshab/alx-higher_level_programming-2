#!/usr/bin/python3
import sys
num = len(sys.argv)
print("{} arguments:".format(num))
for i in range(1, num, 1):
    print("{}: {}".format(i, sys.argv[i]))