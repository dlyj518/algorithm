def ccw(a, b, c): return (b[0] - a[0]) * (c[1] - b[1]) - (c[0] - b[0]) * (b[1] - a[1])
def pdcw(a, b, c, d): return ccw(a, b, c) * ccw(a, b, d)

pt = []
a1, a2, b1, b2 = map(int, input().split())
c1, c2, d1, d2 = map(int, input().split())
a, b, c, d = [a1, a2], [b1, b2], [c1, c2], [d1, d2]
if pdcw(a, b, c, d) <= 0 and pdcw(c, d, a, b) <= 0:
    if not pdcw(a, b, c, d) and not pdcw(c, d, a, b):
        if max(a1, b1) >= min(c1, d1) and max(c1, d1) >= min(a1, b1) and\
            max(a2, b2) >= min(c2, d2) and max(c2, d2) >= min(a2, b2):
            print(1)
        else: print(0)
    else: print(1)
else: print(0)