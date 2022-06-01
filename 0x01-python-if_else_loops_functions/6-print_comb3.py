#!/usr/bin/python3
for j in range(100):
    if j % 10 > j / 10:
        if j != 89:
            print("{:02d}".format(j), end=", ")
        else:
            print("{}".format(j))
