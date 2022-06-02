#!/usr/bin/python3
import sys
num = len(sys.argv)
if __name__ == "__main__":
    if num == 0:
        print("{} arguments:".format(num))
    elif num == 1:
        print("{} arguments:".format(num))
    else: 
        print("{} arguments:".format(num-1))
        for i in range(1, num, 1):
            print("{}: {}".format(i, sys.argv[i]))
