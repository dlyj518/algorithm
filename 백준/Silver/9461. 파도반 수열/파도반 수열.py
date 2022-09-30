x = [0,1,1,1,2,2]
n = int(input())
a = []
for _ in range(n): a.append(int(input()))
for i in range(6,max(a)+1): x.append(x[i-5]+x[i-1])
for z in a: print(x[z])