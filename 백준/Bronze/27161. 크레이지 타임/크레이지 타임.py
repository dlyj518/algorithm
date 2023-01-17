n = int(input())
x = 1; h = 0
for _ in range(n):
    c, i = input().split()
    h = ((h - 1) + x) % 12 + 1
    ch = h == int(i)
    rh = c == 'HOURGLASS'
    sy = 'NO'
    if ch != rh:
        if ch: sy = 'YES'
        else: x *= -1
    print(h, sy)