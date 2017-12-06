a = '4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5'
#a = '0 2 7 0'
b = map(int, a.split())

def maxi():
	m = -1
	for i in range(len(b)):
		if m == -1 or b[i] > b[m]:
			m = i
	return m

dc = {}
count = 0
while True:

	conf = '-'.join(map(str,b))
	if dc.has_key(conf):
		print count
		break
	dc[conf] = 1

	print 'before: %s' % b

	mi = maxi()
	v = b[mi]
	b[mi] = 0

	print 'reseted: %s' % b
	print 'max %i has %i' % (mi, v)

	while v > 0:
		mi = (mi + 1) % len(b)
		b[mi] += 1	 
		v-= 1

	print 'after: %s' % b

	count += 1
