n = int(input())
e = int(input())
nn = {i: [] for i in range(1, n+1)}
s = 0
for _ in range(e):
    k, *l = map(int, input().split())
    if 1 in l:
        for i in l: nn[i].append(s)
        s += 1
    else:
        sl = set()
        for i in l:
            for j in nn[i]: sl.add(j)
        for i in l: nn[i] = list(sl)
for i in range(1, n+1):
    if len(nn[i]) == s: print(i)