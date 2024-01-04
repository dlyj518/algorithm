from itertools import combinations as cb

def df(a, b):
    s = 0
    for i in range(4):
        if a[i] != b[i]: s += 1
    return s

t = int(input())
for _ in range(t):
    n = int(input())
    if n > 32: print(0); x = input(); continue
    r = 12
    for a, b, c in cb(input().split(), 3): r = min(r, df(a, b) + df(a, c) + df(b, c))
    print(r)