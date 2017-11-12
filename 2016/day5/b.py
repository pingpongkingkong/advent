import hashlib 
hash = 'ugkcyxxp'

x = 0
code = [None,None,None,None,None,None,None,None]
found = 0
while found < 8:
	m = hashlib.md5()
	m.update('%s%i' % (hash,x))
	out = m.hexdigest()
	if out.startswith('00000'):
		pos = out[5]
		if pos in '01234567':
			if code[int(pos)] == None:
				found += 1
				code[int(pos)] = out[6]
	x += 1
print ''.join(code)
