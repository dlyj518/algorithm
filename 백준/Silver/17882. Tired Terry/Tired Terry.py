n, p, d = map(int, input().split())
wz = (lambda x: x + x[:p - 1])(input())

ss = [0]

c = 0
for i in range(n + p - 1):
    if wz[i] == 'Z': c += 1
    ss.append(c)

zz = 0
if p == 1: print(wz.count('W'))
else:
    for i in range(p, n + p):
        z = ss[i] - ss[i - p] if i else ss[i]
        if z < d: zz += 1
    print(zz)