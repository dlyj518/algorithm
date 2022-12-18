import sys
sys.setrecursionlimit(10**8)

def mv(a, b):
    if a == b: return 1
    if not a: return 2
    if not (a - b) % 2: return 4
    return 3

def lr(i, l, r):
    global dp
    if i > len(bt) - 2: return 0
    if dp[i][l][r] != -1: return dp[i][l][r]
    dp[i][l][r] = min(lr(i+1, bt[i], r) + mv(l, bt[i]), lr(i+1, l, bt[i]) + mv(r, bt[i]))
    return dp[i][l][r]

bt = list(map(int, input().split()))
dp = [[[-1] * 5 for _ in range(5)] for _ in range(100000)]

print(lr(0, 0, 0))