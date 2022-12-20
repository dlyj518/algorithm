n = int(input())
el = []
for _ in range(n): el.append(list(map(int, input().split())))
el.sort(key=lambda x: x[0])
ls = list(zip(*el))[1]
r = []
for a in ls:
    for i in range(len(r)):
        if r[i] >= a: r[i] = a; break
    else: r.append(a)
print(n - len(r))