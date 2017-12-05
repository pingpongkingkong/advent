a = open('input.txt', 'r').readlines()
b = map(int, a)
i = 0
count = 0

while 1:
	if i >= len(b) or i < 0:
		break
	count += 1
	n = i + b[i]
	b[i] += 1
	i = n
	
print count	

