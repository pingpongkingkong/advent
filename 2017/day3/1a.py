code = 361527

def numberToRing(i):
	count = 0

	ringStart = 1
	ringEnd = 1
	increase = 0

	while i > ringEnd:
		ringStart = ringEnd + 1
		increase += 8	
		ringEnd  += increase
		count    += 1

	return count, ringStart, ringEnd

def getXOffset(i, ringDim):
	print "Doing %i" %i
	rectMax   = (ringDim-1)*4
	rectQuart = rectMax/4
	rectHalf  = rectMax/2

	if i <= rectQuart or i == rectMax:
		x = rectQuart
		y = rectQuart - (i % rectQuart)
	elif i < 2*rectQuart:
		x = rectQuart - (i % rectQuart)
		y = 0 
	elif i < 3*rectQuart:
		x = 0
		y = i % rectQuart
	else:
		x = i % rectQuart
		y = rectQuart
	return x,y

ring, start, end = numberToRing(code)
ringDim    = 1 + (ring * 2)
offset     = code-start
rectOffset = offset+1
xoff,yoff = getXOffset(rectOffset,ringDim)

print 'distance: ', abs(((ringDim-1)/2) - xoff) + abs(((ringDim-1)/2) - yoff)

