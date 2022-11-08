import math

tr = ['  *  ', ' * * ', '*****']
n = int(input())
n = int(math.log2(n//3))
for i in range(n):
    m = 3*(2**i)
    nt = []
    for j in range(len(tr)): nt.append(' ' * m + tr[j] + ' ' * m)
    for j in range(len(tr)): nt.append(tr[j] + ' ' + tr[j])
    tr = nt
for t in tr: print(t)