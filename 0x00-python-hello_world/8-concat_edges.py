#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
         language that combines remarkable power with very clear syntax"
str = f"{str[39:-71] + str[114:120] + str[:6]}"
print(str)