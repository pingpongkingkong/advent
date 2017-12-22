direction=0
g = {}
lines = open('input.txt', 'r').readlines()
y = 0
for l in lines:
	x = 0
	for i in l.rstrip():
		indx = '%i,%i' % (x,y)
		g[indx] = i
		x+=1
	y += 1

ix = len(lines[0].rstrip()) / 2
iy = y / 2

infect = 0

delta = [ (0, -1), (1, 0), (0, 1), (-1, 0) ]
dstr = ['up','right','down','left']

for burst in range(10000):
	print 'coor',ix,iy
	indx = '%i,%i' % (ix,iy)	
	# Check infected
	inf = g.get(indx, '.')
	if inf == '#':
		direction = (direction + 1) % 4
		print 'Infected, cleaning, going right, direction = ', dstr[direction]
		g[indx] = '.'
	else:
		direction = (direction -1) % 4
		print 'Clean, infecting, going left, direction = ', dstr[direction]
		g[indx] = '#'
		infect += 1

	xchange,ychange = delta[direction]
	print "(%s) change = (%i, %i)" % (dstr[direction], xchange,ychange)
	ix += xchange
	iy += ychange

print infect	
