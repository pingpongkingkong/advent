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


for x in [10, 12, 15,16,17,18, 19, 21, 22,23,24,25,26]:
	print '- %i' % x
	ring, start, end = numberToRing(x)

	# 
	ringDim = 1 + (ring * 2)

	offset = x-start
	rectOffset = offset+1

	rectHalf = (ringDim-1)*2
	rectQuart = (ringDim-1)

	rectHalfOffset = rectOffset % rectHalf
	rectQuartOffset = rectOffset % rectQuart

	# If you splict rect on a diagonal, which half of the diagonal are we on.
	rectWhichHalf = (rectOffset / rectHalf ) % 2
	rectWhichQuart = (rectOffset / rectQuart ) % 4

	rectPolarity = 1
	if rectWhichHalf:
		rectPolarity = -1

	# Quarts 1,3 would have changing x-offset from quart
	xOffset = ((rectWhichQuart % 2) * rectQuartOffset * rectPolarity % rectQuart ) 
	yOffset = (((rectWhichQuart+1) % 2) * rectQuartOffset * rectPolarity) % rectQuart

	#print rectWhichQuart
	if rectWhichQuart == 0:
		xOffset = rectQuart 
	elif rectWhichQuart == 2:
		xOffset = 0
	#else:
	#	xOffset = rectQuart - xOffset	

	xoff,yoff = getXOffset(rectOffset,ringDim)
	print "x-offset: ", xoff
	print "y-offset: ", yoff

	# Determine starting point for the offset
	#xStart = ((rectWhichHalf+1)%2)*ringDim 
	
	#print xStart, xOffset, xStart-xOffset

	# Reverse x/y poliartiy depending on side
	#polarity = 1 * (rectSide * -1)

	#print xOffset

	#print ringDim, offset, rectHalf, rectHalfOffset, rectSide

