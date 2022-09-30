n, m = map(int, input().split())
dc = {}
for _ in range(n):
    a, b = input().split()
    dc[a] = b
for _ in range(m):
    print(dc[input()])