phrases = open('input.txt','r').read().split("\n")

def testPhrase(phrase):

	if phrase.lower() != phrase:
		print "Failed tolower"
		return False

	parts = phrase.split(' ');
	occur = {}
	for word in parts:

		s = ''.join(sorted(word))

		if occur.has_key(s):
			return False
		else:
			occur[s] = True


	return True

good = 0
for phrase in phrases:
	if testPhrase(phrase):
		good += 1

print good
	
