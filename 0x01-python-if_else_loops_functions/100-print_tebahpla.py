#!/usr/bin/python3
for x in range(122, 96, -1):
    if x % 2 == 0:
        char = chr(x)
    else:
        char = chr(x - 32)
    print("{}".format(char), end="")
