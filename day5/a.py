import hashlib 
hash = 'ugkcyxxp'

x = 0
code = []
while len(code) < 8:
	m = hashlib.md5()
	m.update('%s%i' % (hash,x))
	out = m.hexdigest()
	if out.startswith('00000'):
		code.append( list(out)[5] )
	x += 1
print ''.join(code)
