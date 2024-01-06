n = int(input())
r = 1 if n % 2 else 0
for i in range(1, n // 2):
    if not (i ** 2 + n) ** 0.5 % 1: r += 1
print(r)