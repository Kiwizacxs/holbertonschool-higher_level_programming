#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
p_number = number
if number < 0:
	p_number = p_number * -1
last_digit = p_number % 10
if number < 0:
	last_digit = last_digit * -1
if last_digit > 5:
	print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit % 10 == 0:
	print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit < 6:
		print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
