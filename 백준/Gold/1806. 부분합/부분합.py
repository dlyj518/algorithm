n, s = map(int, input().split())
ls = list(map(int, input().split()))
a, b = 0, 1
rst = 1e5
sm = sum(ls[:1])
while 1:
    if sm >= s:
        sm -= ls[a]
        rst = min(rst, b - a)
        a += 1
    else:
        b += 1
        if b > n: break
        sm += ls[b-1]
print(rst) if rst != 1e5 else print(0)