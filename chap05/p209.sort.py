x = [[5, 8, 10],
     [7, 3, 2],
     [21, 2, 9],
     [99, 58, 33]]
x.sort(key=lambda x: x[2], reverse=True)
print(x)
