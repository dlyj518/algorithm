dp = [0, 1, 2, 4]
for i in range(4, 1000001):
    dp.append((dp[-1] + dp[-2] + dp[-3]) % (1000000009))
for _ in range(int(input())): print(dp[int(input())])