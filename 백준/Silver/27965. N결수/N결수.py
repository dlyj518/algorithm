def dvs(a, b): return a % k + b % k
def dvp(a, b): return a % k * b % k
def ln(x):
    c = 0
    while x > 0:
        x //= 10
        c += 1
    return c

n, k = map(int, input().split())
x = 0
for i in range(1, n + 1):
    x = dvp(x, 10 ** ln(i))
    x = dvs(x, i)
print(x % k)