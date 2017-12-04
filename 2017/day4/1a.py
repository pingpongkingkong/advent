phrases = open('input.txt','r').read().split("\n")

def testPhrase(phrase):

	if phrase.lower() != phrase:
		print "Failed tolower"
		return False

	parts = phrase.split(' ');
	occur = {}
	for word in parts:
		if occur.has_key(word):
			return False
		else:
			occur[word] = True


	return True

good = 0
for phrase in phrases:
	if testPhrase(phrase):
		good += 1

print good
	
