num_list = list(range(1, 8))
#print(num_list)

def double(x):
    return x *2

#print(double(1))

#ret = map(double, num_list)
#print("処理前", num_list)
#print("処理後", list(ret))

for e in map(double, num_list):
    print(e, end=" ")
