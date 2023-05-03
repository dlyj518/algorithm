x, y = int(input()), 0
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    y += a * b
print('Yes') if x == y else print('No')