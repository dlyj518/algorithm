import math

def slp(x1, y1, x2, y2): return (y2-y1)/(x2-x1) if x1 != x2 else math.inf

n = int(input())
for _ in range(n):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    m1 = slp(x1, y1, x2, y2)
    m2 = slp(x3, y3, x4, y4)
    if math.isclose(m1, m2):
        if math.isclose(m1, slp(x1, y1, x3, y3)): print('LINE')
        else: print('NONE')
    else:
        if m1 == math.inf:
            k = y3 - m2*x3
            x, y = x1, m2*x1 + k
        elif m2 == math.inf:
            k = y1 - m1 * x1
            x, y = x3, m1 * x3 + k
        else:
            k1, k2 = y1 - m1*x1, y3 - m2*x3
            x = (k2-k1)/(m1-m2)
            y = m1*x + k1
        print(f'POINT {x:.2f} {y:.2f}')