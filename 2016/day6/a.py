import itertools
f = open('input.txt', 'r')
y = f.read().replace('\n','')
all = []
for a in range(8):
	most = 0
	mostkey = None
	for k,g in itertools.groupby(sorted(list(y[a::8]))):
		lengroup = len(list(g))
		if lengroup > most:
			most = lengroup
			mostkey = k
	all.append(mostkey)
print ''.join(all)
