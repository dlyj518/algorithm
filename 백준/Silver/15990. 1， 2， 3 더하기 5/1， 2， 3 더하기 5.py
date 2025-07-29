dp = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 1]]
x = int(1e9 + 9)

for i in range(4, 100001):
    dp.append([(dp[i - 1][1] + dp[i - 1][2]) % x, (dp[i - 2][0] + dp[i - 2][2]) % x, (dp[i - 3][1] + dp[i - 3][0]) % x])

for _ in range(int(input())): print(sum(dp[int(input())]) % x)