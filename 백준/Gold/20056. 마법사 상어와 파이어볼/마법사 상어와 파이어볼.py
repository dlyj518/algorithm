import sys
input = sys.stdin.readline

dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
n, m, k = map(int, input().split())
fb = []
for _ in range(m):
    r, c, *o = map(int, input().split())
    fb.append([r-1, c-1] + o)
for _ in range(k):
    rc = {}
    for r, c, w, s, d in fb:
        r = (r + dr[d] * s) % n; c = (c + dc[d] * s) % n
        if rc.get((r, c), 0): rc[r,c].append([w, s, d])
        else: rc[(r, c)] = [[w, s, d]]
    fb = []
    for r, c in rc:
        if len(rc[(r, c)]) > 1:
            [sw, ss, od, ed] = [0]*4
            for w, s, d in rc[(r, c)]:
                sw += w
                ss += s
                if d % 2: od += 1
                else: ed += 1
            sw //= 5; ss //= len(rc[(r, c)])
            dd = 1 if od and ed else 0
            if sw:
                for k in range(4): fb.append([r, c, sw, ss, k*2+dd])
        else: fb.append([r, c] + rc[(r, c)][0])
rst = 0
for f in fb: rst += f[2]
print(rst)