def testline(line):
	last = []
	hyper = 0
	good = 0
	for char in list(line):
		last.insert(0, char)

		if char == '[':
			hyper = 1
		elif char == ']':
			hyper = 0
			
		if len(last) >= 4 and last[0] == last[3] and last[1] == last[2] and last[0] != last[1]:
			if hyper == 1:
				return 0
			else:
				good = 1

	if good:
		return 1
	else:
		return 0
	
tally = 0
for line in open('input.txt','r').readlines():
	line = line.rstrip()
	tally += testline(line)

print tally	
		
