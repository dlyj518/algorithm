n = int(input())
rd = list(input())
boj = ['B', 'O', 'J', 'B']
dp = [-1] * n
dp[0] = 0
for i in range(n):
    if dp[i] < 0: continue
    for a in range(3):
        if rd[i] == boj[a]:
            for j in range(i + 1, n):
                if rd[j] == boj[a + 1]:
                    if dp[j] == -1: dp[j] = dp[i] + (j - i) ** 2
                    else: dp[j] = min(dp[j], dp[i] + (j - i) ** 2)
print(dp[-1])
