from bisect import bisect_left
n = int(input())
ls = list(map(int, input().split()))
dp = [0]*(n)
ej = [-1e11]
for i in range(n):
    if ls[i] > ej[-1]: ej.append(ls[i]); dp[i] = len(ej)-1
    else: dp[i] = bisect_left(ej, ls[i]); ej[dp[i]] = ls[i]
c = max(dp)
r = []
print(c)
for j in range(n-1, -1, -1):
    if dp[j] == c: r.append(ls[j]); c -= 1
print(*r[::-1])