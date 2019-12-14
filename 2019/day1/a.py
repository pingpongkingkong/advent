import math
import os
from functools import reduce

def findFuel(mass):
	return math.floor(float(mass) / 3.0) - 2

lines = open('day1.txt').readlines()
fuel = [findFuel(x) for x in lines]
total = reduce( lambda x, y: x+y, fuel )
print (total)

