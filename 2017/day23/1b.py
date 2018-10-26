d = '''set b 79 .. b=79
set c b  c=79
jnz a 2
jnz 1 5
mul b 100 < YIKES A!=0 CASE STARTS b=7900
sub b -100000 < YIKES  b=107900
set c b < YIKES c=107,900
sub c -17000 < YIKES c=124,900 
sub h -1 ... h=-1 per loop?
set g b .. g = 107,900, c always 124,900
sub g c ..
jnz g 2
jnz 1 3
sub b -17
jnz 1 -6'''

ins = d.split('\n')
ins = map(lambda x: x.rstrip().lstrip(), ins)
regs = {'a':1,'b':0,'c':0,'d':0, 'e':0,'f':0,'g':0,'h':0}
off = 0

def jnz(r, parts):
	if x(parts[1]) != 0:
		return x(parts[2])
	else:
		return 1

def iset(r, parts):
	r[parts[1]] = x(parts[2])
	return 1

def sub(r, parts):
	print "Doing sub: %s" % str(parts)
	print r
	r[parts[1]] = x(parts[1]) - x(parts[2])
	print r
	
	return 1

def mul(r, parts):
	r[parts[1]] = x(parts[1]) * x(parts[2])
	return 1

def x(v):
	global regs
	if v.replace('-','').isdigit():
		return int(v)
	else:
		return int(regs[v]) 
fns =  {'mul':mul, 'set':iset, 'sub':sub, 'jnz':jnz}

count = 0
icount = {}
loop = 0

def show():
	global ins
	global icount
	global regs
	
	countout = []
	indicies = []
	for ikey in sorted(icount.keys()):
		indicies.append(ikey)	
		countout.append(icount[ikey])
			
	print '\n'
	x = zip(indicies, countout, ins)
	print "\n".join(map(lambda y: str(y), x))
	print regs

while off < len(ins):

	loop += 1
	icount[off] = icount.get(off, 0) + 1
	i = ins[off]
	p = i.split()

	#print p
	#raw_input("..")
	#if loop % 100000 == 0:
	#show()
	#print ic
	#print regs
	#print off
	#print p

	if p[0] == 'mul':
		count += 1

	off += fns[p[0]](regs, p)

print loop
print regs
