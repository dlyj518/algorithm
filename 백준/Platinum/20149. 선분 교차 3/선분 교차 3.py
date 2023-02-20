def ans(a, b, c, d):
    print(1)
    px = (a[0] * b[1] - a[1] * b[0]) * (c[0] - d[0]) - (a[0] - b[0]) * (c[0] * d[1] - c[1] * d[0])
    py = (a[0] * b[1] - a[1] * b[0]) * (c[1] - d[1]) - (a[1] - b[1]) * (c[0] * d[1] - c[1] * d[0])
    p = (a[0] - b[0]) * (c[1] - d[1]) - (a[1] - b[1]) * (c[0] - d[0])
    if p == 0:
        if b == c and a <= c: print(b[0], b[1])
        elif a == d and c <= a: print(a[0], a[1])
    else:
        x, y = px / p, py / p
        print(f"{x:.9f} {y:.9f}")

def ccw(a, b, c):
    tmp = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
    tmp -= b[0] * a[1] + c[0] * b[1] + a[0] * c[1]    
    if not tmp: return 0
    else: return tmp // abs(tmp)

def solve(a, b, c, d):
    ans1 = ccw(a, b, c) * ccw(a, b, d)
    ans2 = ccw(c, d, a) * ccw(c, d, b)    
    if not (ans1 or ans2):
        if a > b: a, b = b, a
        if c > d: c, d = d, c    
        if a <= d and b >= c: ans(a, b, c, d)
        else: print(0)
    else:
        if ans1 <= 0 and ans2 <= 0: ans(a, b, c, d)
        else: print(0)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
solve((x1, y1), (x2, y2), (x3, y3), (x4, y4))