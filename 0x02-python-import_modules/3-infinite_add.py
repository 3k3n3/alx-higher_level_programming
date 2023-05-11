#!/usr/bin/python3
import sys

total = 0
if len(sys.argv[1:]) != 0:
    for i in sys.argv[1:]:
        total += int(i)

if __name__ == "__main__":
    print(total)
