def ccw(a, b, c): return (b[0] - a[0]) * (c[1] - b[1]) - (c[0] - b[0]) * (b[1] - a[1])

pt = []
for _ in range(2):
    pp = list(map(int, input().split()))
    pt += [pp[:2], pp[2:]]
if ccw(pt[0], pt[1], pt[2]) * ccw(pt[0], pt[1], pt[3]) < 0 and ccw(pt[2], pt[3], pt[0]) * ccw(pt[2], pt[3], pt[1]) < 0: print(1)
else: print(0)