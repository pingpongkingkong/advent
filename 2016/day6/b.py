import itertools
f = open('input.txt', 'r')
y = f.read().replace('\n','')
all = []
for a in range(8):
	least = 1000000000
	leastkey = None
	for k,g in itertools.groupby(sorted(list(y[a::8]))):
		lengroup = len(list(g))
		if lengroup < least:
			least = lengroup
			leastkey = k
	all.append(leastkey)
print ''.join(all)
