dp = [[0, 0, 0], [1, 0, 0], [1, 1, 0], [2, 0, 1]]

for i in range(4, 10001):
    dp.append([sum(dp[i - 1]), dp[i - 2][1] + dp[i - 2][2], dp[i - 3][2]])

for _ in range(int(input())):
    print(sum(dp[int(input())]))