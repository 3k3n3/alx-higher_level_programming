#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    """Handles basic calculations."""

    if len(sys.argv[1:]) != 3:
        sys.stdout.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif sys.argv[2] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif sys.argv[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif sys.argv[2] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
