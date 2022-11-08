from math import gcd

def pd(x, y):
    if y == 1: return x % b
    xx = pd(x, y//2)
    if not y % 2: return xx * xx % b
    return xx * xx * x % b

b = 10**9+7
m = int(input())
rst = 0
for _ in range(m):
    n, s = map(int, input().split())
    g = gcd(n, s)
    n, s = n//g, s//g
    rst += s * pd(n, b-2)
    rst %= b
print(rst)