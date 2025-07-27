import sys
input = sys.stdin.readline

n = int(input())
xy = []
f = 0
for _ in range(n):
    x, y = map(int, input().split())
    if y < x or y < -x: f += 1
    else: xy.append(x ** 2 + y ** 2)

xy.sort()

q = int(input())
for _ in range(q):
    r = int(input())
    r = r ** 2
    i, j = 0, len(xy) - 1
    while i <= j:
        m = (i + j) // 2
        if xy[m] <= r: i = m + 1
        else: j = m - 1
    print(f, i, len(xy) - i)