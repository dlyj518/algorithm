import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    dt = set()
    ls = []
    for _ in range(n):
        a, b = map(int, input().split())
        dt.add((a, b))
        ls.append((a, b))
    mx = 0
    for i in range(n):
        for j in range(n):
            if i == j: continue
            a, b = ls[i], ls[j]
            dx, dy = b[0] - a[0], b[1] - a[1]
            s = dx ** 2 + dy ** 2
            if s <= mx: continue
            if (a[0] - dy, a[1] + dx) in dt and (b[0] - dy, b[1] + dx) in dt: mx = s
    print(mx)