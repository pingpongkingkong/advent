from itertools import islice, chain
values = map(lambda x: int(x), open('input.txt').read().split())
i0     = chain( islice(values, 0, None, 3), islice(values, 1, None, 3), islice(values, 2,None,3))
print len(filter(lambda x: x[0]+x[1]>x[2], iter(lambda: sorted(list(islice(i0, 3))), [])))
