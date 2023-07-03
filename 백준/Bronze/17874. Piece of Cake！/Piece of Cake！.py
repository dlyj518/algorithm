n, a, b = map(int, input().split())
print(4 * max(a, n - a) * max(b, n - b))