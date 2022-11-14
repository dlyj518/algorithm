n = int(input())
mp = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for i in range(n):
    for j in range(2, n):
        if not mp[i][j]:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
            if i > 0:
                dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]
                if not(mp[i][j-1] or mp[i-1][j]): dp[i][j][1] = sum(dp[i-1][j-1])
print(sum(dp[-1][-1]))