#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = int(str(number)[-1])
if number < 0:
    last_dig *= -1
print("Last digit of {0:d} is {1:d}".format(number, last_dig), end=" ")
if last_dig == 0:
    print("and is 0")
elif last_dig > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
