a = open('input.txt', 'r').readlines()
a = map(lambda x: x.rstrip(), a)
a = set(a)

output = []
def test(target, tiles):

	most = 0
	mostTile = None

	for e in tiles:
		ports=e.split('/')

		if target in ports:

			portCost = sum(map(int, ports))

			ports.remove(target)
			newTarget = ports[0]

			remains = tiles.copy()	
			remains.remove(e)

			newMost = test(newTarget, remains)

			newMost += portCost

			if newMost > most:
				most = newMost

	return most

print test('0', a)
