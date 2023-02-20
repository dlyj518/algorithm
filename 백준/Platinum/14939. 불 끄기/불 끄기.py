def rep(x): return 1 if x == 'O' else 0
def chg(i, j):
            mp[i][j] ^= 1
            if i > 0: mp[i - 1][j] ^= 1
            if i < 9: mp[i + 1][j] ^= 1
            if j < 9: mp[i][j + 1] ^= 1
            if j > 0: mp[i][j - 1] ^= 1
np = [list(map(rep, input().rstrip())) for _ in range(10)]
for n in range(1 << 10):
    c = 0
    mp = [np[i][:] for i in range(10)]
    for i in range(10):
        if not (n & (1 << i)): chg(0, i); c += 1
    q = 0
    for i in range(1, 10):
        for j in range(10):
            if mp[i - 1][j]:
                c += 1; chg(i, j)
    if not sum(sum(mp, [])): print(c); break
else: print(-1)