#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number > 5:
    print(f"the last digit of {number:d} is {last_digit:d} and is greater than 5")
if number == 0:
    print(f"the last digit of {number:d} is {last_digit:d} and is zero")
if number < 6 and not 0:
    print(f"the last digit of {number:d} is {last_digit:d} and less than 6 and not 0")
