import re
input = open('input.txt').read()
output = '';

m = re.compile('^ ([^(]*?) \( (\d+) x (\d+) \) (.*)', re.VERBOSE)

#input = 'A(2x2)BCD(2x2)EF'
#input = '(6x1)(1x3)A'
#input = 'X(8x2)(3x3)ABCY'

while 1:

	print input
	a = m.match(input)
	if a == None:
		output += input
		break
	before, stride, repcount, rest = a.groups()

	output += before + rest[0:int(stride)] * int(repcount)
	print output
	input = rest[int(stride):]
	print 'NEW INPUT: ', input

print "OUTPUT: ", len(output)
