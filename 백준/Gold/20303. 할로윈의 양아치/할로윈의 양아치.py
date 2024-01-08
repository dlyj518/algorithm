import sys
input = sys.stdin.readline

def fnd(x):
    if pr[x] != x: return fnd(pr[x])
    return x
def uni(a, b):
    a, b = fnd(a), fnd(b)
    if a < b: pr[b] = a
    else: pr[a] = b

n, m, k = map(int, input().split())
cn = [0] + list(map(int, input().split()))
pr = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    uni(a, b)

cd = {}
for i in range(1, n + 1):
    pr[i] = fnd(i)
    if cd.get(pr[i], 0): cd[pr[i]][0] += 1; cd[pr[i]][1] += cn[i]
    else: cd[pr[i]] = [1, cn[i]]
cd = list(cd.values())

dp = [0] * (k)
for a, b in cd:
    for i in range(k - 1, a - 1, -1): dp[i] = max(dp[i], dp[i - a] + b)
print(dp[-1])