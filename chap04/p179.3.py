pairs = [(2, 'down'), (1, 'up'), (4, 'charm'), (3, 'strange'), (6, 'top'), (5, 'bottom')]
#print(pairs)
#pairs.sort()
#print(pairs)
#pairs.sort(key=lambda x: x[1])
#print(pairs)
pairs.sort(key=lambda x: x[1], reverse=True)
print(pairs)
