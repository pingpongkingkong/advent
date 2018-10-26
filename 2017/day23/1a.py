d = '''set b 79 .. b=79
set c b  c=79
jnz a 2
jnz 1 5
mul b 100 < YIKES A!=0 CASE STARTS b=7900
sub b -100000 < YIKES  b=107900
set c b < YIKES c=107,900
sub c -17000 < YIKES c=124,900
set f 1 <-- from jnz 1 5 .. A==0 CASE START  f=1
set d 2 d=2
set e 2 <problem e=2
set g d < g=2 << jump target from 20 (when g ne 0) .. d will always be 2 until we pass 20
mul g e < g=4
sub g b < .. b would have been zero before, now g=4-107,900 = 107,904
jnz g 2 .. will be zero when e=53950
set f 0 ...... F=0 is SKIPPED  b cause F to not be 0
sub e -1 .. e=3
set g e .. g=3 53951
sub g b .. g=3-107,900=106,897
jnz g -8 only when e=107900 (and now F=0)
sub d -1 ... 2 - (1 per round)
set g d
sub g b
jnz g -13 only when g=107,900
jnz f 2 ... F not being reset to 0 at 16 causes skipping decrement of h
sub h -1 ... h=-1 per loop?
set g b .. g = 107,900, c always 124,900
sub g c ..  
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23'''

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
	r[parts[1]] = x(parts[1]) - x(parts[2])
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

	if i == 23:
		print p
	#raw_input("..")
	if loop % 100000 == 0:
		show()
	#print ic
	#print regs
	#print off
	#print p

	if p[0] == 'mul':
		count += 1

	off += fns[p[0]](regs, p)


print regs
