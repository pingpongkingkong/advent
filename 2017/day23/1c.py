d = '''set b 79 b=79
set c b c=79
jnz a 2 
jnz 1 5
mul b 100 b=7,900
sub b -100000 b=107,900
set c b c=107,900
sub c -17000 c=124,900
set f 1 f=1									TARGET of 32
set d 2 d=2
set e 2 e=2									TARGET of 24 -13 JNZ
set g d g=d=2 =                               TARGET OF 20. JNZ
mul g e g = g*2 = d*2 = 2*2 = 4 ALWAYS
sub g b g = 4-107,900=-106,896
jnz g 2
set f 0
sub e -1 e=3 								TARGET of 15. 
set g e g=3
sub g b g=g-107,900
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23'''

breaks = [24]
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

	if i == 15:
		show()
		raw_input("..")
	#print ic
	#print regs
	#print off
	#print p

	if p[0] == 'mul':
		count += 1

	off += fns[p[0]](regs, p)


print regs
