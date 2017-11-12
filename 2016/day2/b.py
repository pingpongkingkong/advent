def isValid(x,y):
	if (x < 0 or y < 0 or x > 4 or y > 4):
		return False

	# Bounds are symmetrical, so below bounds can be considered organized x by y, or y by x
	bounds = ((2,2), (1,3), (0,4), (1,3), (2,2))
	if x != max( bounds[y][0], min( bounds[y][1], x) ) or \
	       y != max( bounds[x][0], min( bounds[x][1], y) ):
		return False

	return True
		
delta   = { 'U' : [0,-1], 'D' : [0,1], 'L':[-1,-0], 'R':[1,0] }
x       = 0
y       = 2
for line in open('input.txt', 'r').read().rstrip().split('\n'):
	for code in line.rstrip():
		#print 'code : %s' % code
		newx = x+delta[ code ][0]
		newy = y+delta[ code ][1]
		if isValid(newx, newy):
			(x,y) = (newx,newy)
		#print x,y
	print (list('__1__'), list('_234_'), list('56789'), list('_ABC_'), list('__D__'))[y][x]

