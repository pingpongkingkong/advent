print len(filter(lambda x: x[0]+x[1]>x[2], [sorted(map(lambda x: int(x), line.rstrip().split())) for line in open('input.txt').readlines()]))
