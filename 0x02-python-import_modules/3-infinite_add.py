#!/usr/bin/python3
import sys
num = len(sys.argv)
sum = 0
for i in range(1, num, 1):
    sum = sum + int(sys.argv[i])
print(sum)
