from math import gcd
n = int(input())
dt = {}
mx = 1
for _ in range(n):
    x, y = map(int, input().split())
    g = gcd(x, y)
    x //= g; y //= g
    if dt.get((x, y), 0):
        dt[(x, y)] += 1
        if dt[(x, y)] > mx: mx = dt[(x, y)]
    else: dt[(x, y)] = 1
print(mx)