a, b, c = map(int, input().split())
a -= 1; b -= 1
print((a // c + 1) * (b // c + 1))