n = int(input())
ls = list(map(int, input().split()))
sc = [0] * 1000001
ch = sc[:]
for i in ls: ch[i] = 1
for i in sorted(ls):
    for j in range(i * 2, 1000001, i):
        if ch[j]: sc[i] += 1; sc[j] -= 1
for i in ls: print(sc[i], end=' ')