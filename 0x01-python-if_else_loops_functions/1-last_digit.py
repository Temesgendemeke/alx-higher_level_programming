#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nx = number % 10
print(f"Last digit of {number:d} is {nx:d}")
