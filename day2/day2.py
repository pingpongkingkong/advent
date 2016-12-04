delta   = { 'U' : [0,-1], 'D' : [0,1], 'L':[-1,-0], 'R':[1,0] }
x       = y = 1
for line in open('input.txt', 'r').read().rstrip().split('\n'):
	for code in line.rstrip():
		x += delta[ code ][0]
		y += delta[ code ][1]
		x = max(0, min(2, x))
		y = max(0, min(2, y))
	print ((1,2,3),(4,5,6),(7,8,9))[y][x]
