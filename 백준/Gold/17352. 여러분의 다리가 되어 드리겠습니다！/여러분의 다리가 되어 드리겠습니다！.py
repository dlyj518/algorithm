import sys
input = sys.stdin.readline

def fnd(i):
    if i == pr[i]: return i
    return fnd(pr[i])

n = int(input())
s, pr = set(), list(range(n + 1))
for _ in range(n - 2):
    a, b = map(fnd, map(int, input().split()))
    if a > b: a, b = b, a
    pr[b] = a
for i in range(1, n + 1): s.add(fnd(pr[i]))
for i in s: print(i, end=' ')