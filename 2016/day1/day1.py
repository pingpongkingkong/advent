import os, math

dir     = 0 
delta   = { 0 : [0,1], 1 : [1,0], 2:[0,-1], 3:[-1,0] }
mapping = {'R':1, 'L':-1}
x       = y = 0
for op in open('input.txt', 'r').read().rstrip().split(', '):
	#print x, y, op, 
	dir = (dir + mapping[op[0]]) % 4
	x += delta[ dir ][0] * int(op[1:])
	y += delta[ dir ][1] * int(op[1:])
print abs(x) + abs(y)
