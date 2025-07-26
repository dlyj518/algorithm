n, m = map(int, input().split())
lm = list(map(int, input().split()))
ni = [[] for _ in range(n)]
gm = [[] for _ in range(m + 1)]

for i in range(n):
    sg = list(map(int, input().split()))
    for s in sg:
        if s == -1: break
        gm[s].append(i)

for i in range(1, m + 1):
    if len(gm[i]) > lm[i - 1]:
        lm[i - 1] = 0
    else:
        for j in gm[i]:
            ni[j].append(i)
        lm[i - 1] -= len(gm[i])
        gm[i] = []

for i in range(n):
    sg = list(map(int, input().split()))
    for s in sg:
        if s == -1: break
        gm[s].append(i)

for i in range(1, m + 1):
    if len(gm[i]) > lm[i - 1]:
        lm[i - 1] = 0
    else:
        for j in gm[i]:
            ni[j].append(i)
        gm[i] = []

for i in range(n):
    if ni[i]: print(*sorted(ni[i]))
    else: print('망했어요')