m = 1e5
a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
for i in [a, b, c]:
    m = min(m, min(i + d, i + e))
print(m - 50)