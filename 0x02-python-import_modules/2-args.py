#!/usr/bin/python3
import sys

if __name__ == "__main__":
    if len(sys.argv[1:]) > 1:
        print("{} arguments:".format(len(sys.argv[1:])))
        for enum, i in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(enum, i))

    elif len(sys.argv[1:]) == 1:
        print("1 argument:\n1: {}".format(sys.argv[1]))

    else:
        print("0 arguments.")
