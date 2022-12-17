p, m = map(int ,input().split())
rm = []
for _ in range(p):
    l, n = input().split()
    l = int(l)
    for i in range(len(rm)):
        if rm[i][0][0] - 10 <= l <= rm[i][0][0] + 10 and len(rm[i]) < m: rm[i].append([l, n]); break
    else: rm.append([[l, n]])
for l in rm:
    if len(l) == m: print('Started!')
    else: print('Waiting!')
    l.sort(key=lambda x: x[1])
    for a in l: print(*a)