from math import factorial as f

def dfs(m, rr, gg, bb):
    if m > n: return 1
    if dp[m][rr][gg][bb] != -1: return dp[m][rr][gg][bb]
    c = 0
    for i in range(min(n, rr)+1):
        for j in range(min(n-i, gg)+1):
            k = m-i-j
            if k > bb or k < 0: continue
            tt = []
            for t in [i, j, k]:
                if t: tt.append(t)
            if max(tt) != min(tt): continue
            c += dfs(m+1, rr-i, gg-j, bb-k) * f(i+j+k)//(f(i)*f(j)*f(k))
    dp[m][rr][gg][bb] = c
    return c

n, r, g, b = map(int, input().split())
dp = [[[[-1]*56 for _ in range(56)] for _ in range(56)] for _ in range(n+1)]
print(dfs(1, r, g, b))