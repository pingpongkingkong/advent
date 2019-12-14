import math
import os
from functools import reduce

def findFuel(mass):
	aMass = math.floor(float(mass) / 3.0) - 2
	if aMass < 0:
		return 0
	else:
		return aMass + findFuel(aMass)


lines = [1969]
lines = [100756]
lines = open('day1.txt').readlines()
fuel = [findFuel(x) for x in lines]
total = reduce( lambda x, y: x+y, fuel )
print (total)

