import os, math

dir     = 0 
delta   = { 0 : [0,1], 1 : [1,0], 2:[0,-1], 3:[-1,0] }
mapping = {'R':1, 'L':-1}
x       = y = 0
hit     = {'0,0':1}
for op in open('input.txt', 'r').read().rstrip().split(', '):
	dir = (dir + mapping[op[0]]) % 4
	newx = delta[ dir ][0] * int(op[1:])
	newy = delta[ dir ][1] * int(op[1:])

	if delta[dir][0] != 0:
		for walkx in range(delta[dir][0], newx + delta[dir][0], delta[dir][0]):
			coord = '%i,%i' % (x+walkx, y)
			if coord in hit:
				print coord
			hit[coord] = 1

	if delta[dir][1] != 0:
		for walky in range(delta[dir][1], newy + delta[dir][1], delta[dir][1]):
			coord = '%i,%i' % (x, y+walky)
			if coord in hit:
				print coord
			hit[coord] = 1

	x += newx
	y += newy
