from math import gcd
t = int(input())
dp = [0] * 1001
dp[1] = 3
for i in range(2, 1001):
    c = 0
    for j in range(1, i):
        if gcd(i, j) == 1: c += 1
    dp[i] = dp[i - 1] + c * 2
for _ in range(t): print(dp[int(input())])