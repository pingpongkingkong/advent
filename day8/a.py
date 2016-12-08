pix = []
for y in range(6):
	for x in range(50):
		pix.append(' ')

def setPixel(p,x,y,v):
	p[ y * 50 + x] = v

def getPixel(p,x,y):
	return p[(y * 50) + x]
			
for ins in open('input.txt').readlines():
	ins = ins.rstrip()

	if ins.startswith('rotate column x'):
		parts  = ins.split(' ')
		column = parts[2].split('=')[1]
		amount = int(parts[4])
		newPix = list(pix)
		for i in range(6):
			setPixel(newPix, int(column), i, getPixel(pix, int(column), (6-amount+i)%6))
		pix = newPix
			

	elif ins.startswith('rotate row '):
		parts  = ins.split(' ')
		row    = parts[2].split('=')[1]
		amount = int(parts[4])
		newPix = list(pix)
		for i in range(50):
			setPixel(newPix, i, int(row), getPixel(pix, (50-amount+i)%50, int(row)))
		pix = newPix

	elif ins.startswith('rect '):
		(x,y) = ins.split(' ')[1].split('x')
		for pY in range(int(y)):
			for pX in range(int(x)):
				setPixel(pix, pX, pY, '#')
	
lit = 0
for y in range(6):
	for x in range(50):
		print getPixel(pix, x,y), 
		if getPixel(pix, x,y) == "#":
			lit += 1
	print "\n"
print lit
