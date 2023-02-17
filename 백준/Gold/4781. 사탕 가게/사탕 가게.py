import sys
input = sys.stdin.readline

while 1:
    n, m = map(float, input().split())
    if n == m == 0: break
    n, m = map(int, (n, m * 100 + .5))
    ls = []
    for _ in range(n):
        a, b = input().split()
        ls.append(list(map(int, (a, float(b) * 100 + .5))))
    dp = [0] * (m + 1)
    for i in range(n):
        for j in range(1, m + 1):
            x = j - ls[i][1]
            if x >= 0: dp[j] = max(dp[j], dp[x] + ls[i][0])
    print(dp[-1])