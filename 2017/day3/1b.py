
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

# Gets offset from rectangle origin (0,0), not from the centre point origin.
def getXOffset(i, ringDim):
	rectMax   = (ringDim-1)*4
	rectQuart = rectMax/4

	#print "rectoffset=%i - ring dimension (%i) quarter size (%i) max size (%i)" % (i, ringDim, rectQuart, rectMax)

	if i == rectMax:
		x = rectQuart
		y = rectQuart
	elif i <= rectQuart:
		x = rectQuart
		y = rectQuart - i 
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


def getOffsets(code):

	if code == 1:
		return (0,0)

	ring, start, end = numberToRing(code)
	ringDim    = 1 + (ring * 2)
	#print "%i is in (%i)th ring, which has dimension %i and S/E (%i -> %i)" % (code, ring, ringDim, start, end)
	offset     = code-start
	rectOffset = offset+1
	xoff,yoff = getXOffset(rectOffset,ringDim)

	#print 'yoff: ',yoff
	#print ringDim
	xDistance = xoff-((ringDim-1)/2)
	yDistance = yoff - ((ringDim-1)/2) 

	return xDistance, yDistance


cache = {'0/0':1}
counter = 2
target = 361527
while True:
	code = counter
	running = 0
	if counter % 10000 == 0:
		print "%i/%i" % (counter, target)
	x,y = getOffsets(code)
	offHash = '%i/%i' % (x,y)
	#print 'Current code (%i) hash (%s)' % (code, offHash)
	for offX,offY in [ (-1,-1), (0, -1), (1,-1), (-1, 0), (1, 0), (-1,1), (0,1), (1,1) ]:
		newHash = '%i/%i' % ((x + offX), (y+offY))
		value = cache.get(newHash, 0)
		#print "Got cached value %s - %i" % (newHash, value)
		running += value

	#print "SETTING CODE: %i (%s): %i" % (code, offHash, running)
	cache[offHash] = running
	
	if running > target:
		print running
		break
	counter += 1

