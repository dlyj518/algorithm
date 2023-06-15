n = int(input()); m = 1e5
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b: m = min(b, m)
print(m) if m != 1e5 else print(-1)