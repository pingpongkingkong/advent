a = open('in.txt', 'r').readlines()

items = {}
class item:
	def __init__(self, name, weight, children):
		self.name = name
		self.weight = weight
		self.children = children
		self.parent = None

for line in a:
	parts = line.strip().split(' ',3)
	name, weight = parts[0:2]

	weight=int(weight.replace("(",'').replace(")",""))
	if items.has_key(name):
		i = items[name]
		i.weight = weight
	else:
		i = item(name, weight, [])
		items[name] = i

	if len(parts) > 2:
		childnames = [x.strip() for x in parts[3].split(',')]
		
		for n in childnames:

			if items.has_key(n):
				c = items[n]
			else:
				c = item(n, None, [])
				items[n] = c
				
			c.parent = i		

			i.children.append(c)
	

while True:
	if i.parent == None:
		print 'Root is: %s' % i.name
		break
	i = i.parent	

def od_printit(x, depth):
	print '%s N: %s W: %s' % (' '*depth, x.name, x.weight)
	weights = [(printit(y, depth+1), y.name, y.parent.name) for y in x.children]

	print '%s allweights %s' % (depth*' ',weights)

	s = sum([y[0] for y in weights])

	s += x.weight
	print "sum is %i" % s

	if len(weights) == 0:
		return s

	(wl,nl, pl) = weights.pop()
	print "%sTW for %s is %s" % (depth*' ', nl, wl)
	
	for (w,n,p) in weights:
		print "%sTW for %s is %s" % (depth*' ', n, w)
		if w != wl:
			print "%sUnmatching weight is either %i (%s/%s) or %i (%s/%s)" % (depth*' ',wl, nl, pl, w, n, p)
			wl = w
			nl = n	
		
	return s

def calcweight(x):
	s = sum([calcweight(y) for y in x.children])
	x.total = s + x.weight
	x.childweight = s
	return x.total

def printTree(x,depth):

	print "%s %s (%i) (%i)" % (depth*' ', x.name, x.total, x.childweight)

	
	for c in x.children:
		print '- %s %s (%i) (%i)' % (depth*' ', c.name, c.total, c.childweight)

	for c in x.children:
		printTree(c, depth+1)

def printit(x, depth):
	print '%s N: %s W: %s' % (' '*depth, x.name, x.weight)
	weights = [(printit(y, depth+1), y.name, y.parent.name) for y in x.children]

	print '%s allweights %s' % (depth*' ',weights)

	s = sum([y[0] for y in weights])

	print "%s %s child weights %i" % (depth * ' ', x.name, s)

	s += x.weight

	print "%s final sum %s is %i" % (depth*' ',x.name, s)

	if len(weights) == 0:
		return s

	(wl,nl, pl) = weights.pop()
	print "%sTW for %s is %s" % (depth*' ', nl, wl)
	
	for (w,n,p) in weights:
		print "%sTW for %s is %s" % (depth*' ', n, w)
		if w != wl:
			print "%sUnmatching weight is either %i (%s/%s) or %i (%s/%s)" % (depth*' ',wl, nl, pl, w, n, p)
			wl = w
			nl = n	
		
	return s
printit(i,0)

#calcweight(i)
#printTree(i,0)	
