# -*- coding: cp1252 -*-
import random

print("Throw a coin five times:")
for i in range(5):
    number = random.randint(0,1)
    if number == 0:
        print("Tails!")
    else:
        print("Crowns!")