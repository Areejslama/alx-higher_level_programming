#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit < 0:
    last_digit = -last_digit
    print("last digit of {} is {}".format(number, last_digit),  end="")
elif last_digit > 5:
    print("is greater than 5")
elif last_digit == 0:
    print("is zero")
else:
    print("is less than 6 and not 0")
