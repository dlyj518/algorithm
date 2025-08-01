n, m, k = map(int, input().split())
a = sum(list(map(int, input().split())))
b = sum(list(map(int, input().split())))
si = list(map(int, input().split()))

for s in si:
    x = min(s, a)
    y = min(s, b + x)
    a += y - x
    b += x - y

print(abs(n - a - b))