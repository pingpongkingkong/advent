import math
import os
import operator as op
from functools import reduce
import sys
def findFuel(mass):
	return math.floor(float(mass) / 3.0) - 2

linesOrig = [int(x) for x in open('day2.txt').read().split(',')]
#lines = [1,0,0,0,99]
#lines = [1,1,1,4,99,5,6,0,99]

for a in range(0, 100):
	for b in range(0,100):
		lines = list(linesOrig)
		lines[1] = a
		lines[2] = b
		i = 0
		while i < len(lines):
			op = lines[i]
			if op == 99:
				break
			op1 = lines[ lines[i+1] ]
			op2 = lines[ lines[i+2] ]
			op3 = lines[i+3] 
			if op == 1:
				lines[op3] = op1 + op2
				#print("add: %i %i %i" % (op1, op2, op3 ) )
				#print 'after', lines
			elif op == 2:
				#print("mul")
				lines[op3] = op1 * op2
				#print 'after', lines
			else:
				print "Err at ??"
				break
			i += 4

		if lines[0] == 19690720:
			print (a, b)

print "Done"
