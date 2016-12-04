import re, itertools
def sorter(x,y):
	presort = cmp(y[1], x[1])
	return presort if presort != 0 else cmp(x[0], y[0])

t = 0
for line in open('input.txt').readlines():
	r,s,c0 = re.match(r'^(.*)-(\d+)\[(\w+)\]$', line).groups()
	sorts = sorted( map( lambda x: (x[0], len(list(x[1]))), itertools.groupby( sorted(list(r.replace('-',''))), ord) ), cmp=sorter)
	c1 = ''.join(map(chr, zip(*sorts[:5])[0]))

	if c1 == c0:
		t += int(s)
print t
