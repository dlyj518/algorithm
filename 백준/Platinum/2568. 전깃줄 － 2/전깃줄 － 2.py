import sys
input = sys.stdin.readline

n = int(input())
el = {}
for _ in range(n):
    a, b = map(int,input().split())
    el[b] = a
it = sorted(el.items(), key=lambda x: x[1])
ls = list(zip(*it))[0]
r = []
l = []
for a in ls:
    for i in range(len(r)):
        if r[i] >= a: l.append(i + 1); r[i] = a; break
    else: l.append(len(r)+1); r.append(a)
x = []
t = len(r)
print(n - t)
for k in range(n-1, -1, -1):
    if l[k] == t: t -= 1
    else: x.append(it[k][1])
print(*reversed(x), sep='\n')