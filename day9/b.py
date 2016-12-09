# FAILED attempt at part 2.

import re
input = open('input.txt').read()

m = re.compile('^ ([^(]*?) \( (\d+) x (\d+) \) (.*)', re.VERBOSE)

def getLen(input):
	a = m.match(input)
	if a == None:
		return len(input)

	before, stride, repcount, rest = a.groups()

	return len(before) + getLen( (rest[0:int(stride)] * int(repcount)) + rest[int(stride):] )


print "OUTPUT: ", getLen(input)
