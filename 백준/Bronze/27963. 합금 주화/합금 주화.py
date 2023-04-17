a, b, c = map(int, input().split())
if a < b: a, b = b, a
print(100 * a * b / (c * (b - a) + a * 100))