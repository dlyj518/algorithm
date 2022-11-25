import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    pr = {i+1: [] for i in range(n)}
    od = {i+1: [] for i in range(n)}
    for _ in range(k):
        a, b = map(int, input().split())
        od[a].append(b)
        pr[b].append(a)
    w = int(input())
    dp = [0]*(n+1)
    while 1:
        q = []
        for i in range(1, n+1):
            if not pr[i]:q.append(i)
        if not q: break
        for x in q:
            dp[x] += d[x]
            for y in od[x]:
                dp[y] = max(dp[y], dp[x])
                pr[y].remove(x)
            pr[x] = [-1]
    print(dp[w])