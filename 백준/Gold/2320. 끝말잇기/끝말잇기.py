def sv(i, j):
    if j == (1 << n) - 1: return 0
    l = me[wd[i][-1]]
    if dp[l][j] != -1: return dp[l][j]
    r = 0
    for k in range(n):
        if j & (1 << k): continue
        if l != me[wd[k][0]]: continue
        r = max(r, sv(k, j | (1 << k)) + len(wd[k]))
    dp[l][j] = r
    return r

n = int(input())
me = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
wd = []
dp = [[-1] * (1 << n) for _ in range(5)]
for _ in range(n): wd.append(input())
rs = 0
for i in range(n): rs = max(rs, sv(i, 1 << i) + len(wd[i]))
print(rs)