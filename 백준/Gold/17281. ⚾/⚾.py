from itertools import permutations

n = int(input())
pl = [list(map(int, input().split())) for _ in range(n)]
pp = list(range(1,9))
rst = 0
for t in permutations(pp, 8):
    t = list(t)
    t = t[:3] + [0] + t[3:]
    s = 0
    c = 0
    for i in range(n):
        o = 0
        b1, b2, b3 = 0, 0, 0
        while o < 3:
            r = pl[i][t[c]]
            if r == 0: o += 1
            if r == 1: s += b3; b1, b2, b3 = 1, b1, b2
            if r == 2: s += b2+b3; b1, b2, b3 = 0, 1, b1
            if r == 3: s += b1+b2+b3; b1, b2, b3 = 0, 0, 1
            if r == 4: s += b1+b2+b3+1; b1, b2, b3 = 0, 0, 0
            c = (c+1)%9
    rst = max(rst, s)
print(rst)