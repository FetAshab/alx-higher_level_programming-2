#!/usr/bin/python3
import sys
num = len(sys.argv)
sum = 0
if __name__ == "__main__":
    for i in range(1, num, 1):
        sum = sum + int(sys.argv[i])
print(sum)
