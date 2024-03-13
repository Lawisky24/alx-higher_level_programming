#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10
if number >= 0
    else number % -10
if lastdigit > 5:
    print(f"Last digit of {:d} is {lastdigit} and is greater than 5")
elif lastdigit < 6 and lastdigit != 0:
    print(f"Last digit of {:d} is {lastdigit} and is less than 6 and not 0")
else:
    print(f"Last digit of {:d} is 0 and is 0")
