import re
input = open('input.txt').read()
output = '';

m = re.compile('^ ([^(]*?) \( (\d+) x (\d+) \) (.*)', re.VERBOSE)

def getLength(input):

	a = m.match(input)

	if a == None:
		return len(input)

	before, stride, repcount, rest = a.groups()

	return len(before) + (int(repcount) * getLength(rest[0:int(stride)])) + getLength(rest[int(stride):])

print "OUTPUT: ", getLength(input)
