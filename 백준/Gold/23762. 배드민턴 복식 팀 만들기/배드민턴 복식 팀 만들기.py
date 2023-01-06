n = int(input())
st = sorted(enumerate(list(map(int, input().split()))), key=lambda x: x[1])
idx = []; pl = []
for i, x in st: idx.append(i); pl.append(x)
sm = [1e9] * n
for i in range(3, n): sm[i] = pl[i] - pl[i - 3]
ls = [[0], [0, 1], [0, 1, 2], []]
dp = [0] * n
dp[3] = sm[3]
for i in range(4, n):
    if i % 4 == 3: dp[i] = dp[i - 4] + sm[i]; ls.append([])
    else:
        if dp[i - 1] < sm[i] + dp[i - 4]:
            dp[i] = dp[i - 1]; ls.append(ls[i-1] + [i])
        else: dp[i] = sm[i] + dp[i - 4]; ls.append(ls[i - 4]) 
print(dp[-1])
for a in ls[-1]: print(idx[a])