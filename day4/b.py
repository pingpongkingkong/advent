from itertools import groupby
import re
def sorter(x,y):
	presort = -cmp(x[1], y[1])
	return presort if presort != 0 else cmp(x[0], y[0])


for line in open('input.txt').readlines():
	match = re.match(r'^(.*) - (\d+) \[ (\w+) \]$', line, re.VERBOSE)
	if not match:
		print 'BAD INPUT: ', line
		exit(1)

	roomname  = match.group(1).replace('-','')
	sector    = int(match.group(2))
	checksum  = match.group(3)

	sorts     = sorted( map( lambda x: (x[0], len(list(x[1]))), groupby( sorted(list(roomname)), lambda x: ord(x)) ), cmp=sorter)
	top5      = ''.join(map(lambda x: chr(x), zip(*sorts[:5])[0]))
	
	if top5 == checksum:
		output = ''
		for letter in list(roomname):
			if letter == '-':
				output += ' '
			else:
				output += chr( ord('a') + (ord(letter) - ord('a') + sector) % 26)
		if output=='northpoleobjectstorage':
			print output, sector
