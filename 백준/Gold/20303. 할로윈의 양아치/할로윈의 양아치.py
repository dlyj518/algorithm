import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
cn = [0] + list(map(int, input().split()))
tr = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    tr[a].append(b); tr[b].append(a)

vs = [1] * (n + 1)
dp = [0] * k
for i in range(1, n + 1):
    if vs[i]:
        w = c = vs[i] = 0
        st = [i]
        while st:
            x = st.pop()
            w += 1; c += cn[x]
            for a in tr[x]:
                if vs[a]: vs[a] = 0; st.append(a)
        for i in range(k - 1, w - 1, -1): dp[i] = max(dp[i], dp[i - w] + c)
print(dp[-1])