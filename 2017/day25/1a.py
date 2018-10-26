ins = map(lambda x: x.rstrip(), open('input.txt','r').readlines())
import os

class SymbolAction:
	def __init__(self):
		self.write = None
		self.move = None
		self.next = None
	def __repr__(self):
		return '<write: %s  move: %s  next: %s>' % (self.write, self.move, self.next)

class State:
	def __init__(self, label):
		self.label = label
		self.symbols = {}

	def __repr__(self):
		return '%s: [%s]' % (self.label, self.symbols)

x = '''In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state F.'''

# Begin in state A.
# Perform a diagnostic checksum after 12964419 steps.

import re
def parse(instruct):

	oState = None
	oSymbol = None

	dStates = {}

	for l in instruct:

		if l == '':
			continue

		m = re.match('\s*In state (\w+):', l)
		if m != None:
			state = m.group(1)
			oState = State(state)	
			dStates[state] = oState

			print 'In state',state
			continue
	
		m = re.match('\s*If the current value is (\d)', l)
		if m != None:
			curvalue= m.group(1)
			oSymbol = SymbolAction()
			oState.symbols[curvalue] = oSymbol

			print 'curvalue',curvalue
			continue


		m = re.match('\s*- Write the value (\d)', l)
		if m != None:
			newvalue= m.group(1)
			oSymbol.write = newvalue

			print 'Newvalue',newvalue
			continue


		m = re.match('\s*- Move one slot to the (left|right).', l)
		if m != None:
			newdir = m.group(1)
			oSymbol.move = newdir
			print 'newdir',newdir
			continue


		m = re.match('\s*- Continue with state (\w).', l)
		if m != None:
			newstate = m.group(1)
			oSymbol.next = newstate
			print 'newstate',newstate

			continue

		print "NO MATCH: %s" % l

		os.exit(0)

	return dStates
#parse(x.split("\n"))
dState=parse(ins)


tape = {}
cursor = 0
state = 'A'

for i in xrange(12964419):
	value = tape.get(cursor, '0')
	ins = dState[state].symbols[value]

	tape[cursor] = ins.write
	if ins.move == 'right':
		cursor += 1
	else:
		cursor -= 1
	state = ins.next
	
print  sum(map(int, tape.values()))
	
	
