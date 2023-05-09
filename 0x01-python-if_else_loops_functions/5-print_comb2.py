#!/usr/bin/python3
for x in range(0, 99):
    if x < 10:
        x = str(0) + str(x)
    print("{},".format(x), end=" ")
print(99)
