#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = int(str((number))[-1])
if number < 0:
    last_dig *= -1
if last_dig == 0:
    print("Last digit of {0} is {1} and is 0".format(number, last_dig))
elif last_dig > 5:
    print("Last digit of {0} is {1} and is\
 greater than 5".format(number, last_dig))
else:
    print("Last digit of {0} is {1} and is\
 less than 6 and not 0".format(number, last_dig))
