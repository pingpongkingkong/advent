a = open('input.txt', 'r').readlines()
a = map(lambda x: x.rstrip(), a)
a = set(a)

def test(target, tiles):
	global g
	most       = 0
	mostLength = 0

	for e in tiles:
		ports=e.split('/')

		if target in ports:

			portCost = sum(map(int, ports))

			ports.remove(target)
			newTarget = ports[0]

			remains = tiles.copy()	
			remains.remove(e)

			newMost, newLength = test(newTarget, remains)

			newMost += portCost
			newLength += 1

			if newLength >= mostLength:
				mostLength = newLength

				if newMost > most:
					most = newMost

	return most, mostLength

print test('0', a)
