x, y = map(int, input().split())
a, b, c = 100 - x, 100 - y, x + y - 100
d = a * b
q, r = d // 100, d % 100
print(a, b, c, d, q, r)
print(c + q, r)