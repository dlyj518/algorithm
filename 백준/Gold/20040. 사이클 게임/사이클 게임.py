import sys
input = sys.stdin.readline

def fnd(x):
    if x == pr[x]: return x
    return fnd(pr[x])

n, m = map(int, input().split())
pr = list(range(n))
for i in range(m):
    a, b = map(fnd, map(int, input().split()))
    if a == b: print(i+1); break
    if a < b: pr[b] = a
    else: pr[a] = b
else: print(0)