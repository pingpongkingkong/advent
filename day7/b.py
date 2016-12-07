def testline(line):
	last = []
	hyper = 0
	good = 0
	inside = []
	outside = []
	for char in list(line):
		last.insert(0, char)

		if char == '[':
			hyper = 1
		elif char == ']':
			hyper = 0
			
		if len(last) >= 3 and last[0] == last[2] and last[0] != last[1]:
			if hyper:
				inside.append(''.join(last[:3]))
			else:
				outside.append(''.join(last[:3]))
	for outer in outside:
		compliment = outer[1] + outer[0] + outer[1]
		if compliment in inside:
			return 1
	return 0
	
tally = 0
for line in open('input.txt','r').readlines():
	line = line.rstrip()
	tally += testline(line)
print tally	
		
