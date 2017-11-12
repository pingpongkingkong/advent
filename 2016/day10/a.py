import re 
from collections import defaultdict

bots   = defaultdict(list)
output = defaultdict(list)
giving = {}

bots['type'] = 'bot'
output['type'] = 'output'

botGives = re.compile('bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)')
valueGoes = re.compile('value (\d+) goes to bot (\d+)')

for line in open('input.txt').readlines():
	if botGives.match(line):
		botId, lowType, lowOut, highType, highOut = botGives.match(line).groups()

		giving[botId] = (bots if lowType=='bot' else output, lowOut, bots if highType=='bot' else output, highOut)


	elif valueGoes.match(line):
		value, botId = valueGoes.match(line).groups()
		bots[botId].append( int(value) )


movement = 1

while movement == 1:

	movement = 0
	for botId in bots.keys():
		if botId == 'type':
			continue

		if len(bots[botId]) == 2:
			movement = 1

			lowType,lowOut,highType,highOut = giving[botId]

			valueLow, valueHigh = sorted(bots[botId])

			if 17 in bots[botId] and 61 in bots[botId]:
				print 'bot %s giving %i to %s %s and %i to %s %s' % (botId, valueLow, lowType['type'], lowOut, valueHigh, highType['type'], highOut)


			lowType[ lowOut ].append( valueLow ) 
			highType[ highOut ].append( valueHigh )

			bots[botId] = []
			

print output['0'][0]*output['1'][0]*output['2'][0]

