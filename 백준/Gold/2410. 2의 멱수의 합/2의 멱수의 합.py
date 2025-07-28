dp = [1]
for i in range(1, int(input()) + 1):
    if i % 2: dp.append(dp[-1])
    else: dp.append(int((dp[-1] + dp[i // 2]) % 1e9))
print(dp[-1])