import sys
input = sys.stdin.readline

def fnd(x):
    if pr[x] != x: return fnd(pr[x])
    return x

v, e = map(int, input().split())
pr = list(range(v+1))
ls = []
for _ in range(e): ls.append(list(map(int, input().split())))
ls.sort(key=lambda x: x[2])
rst = 0
for a, b, c in ls:
    if v < 3: break
    a, b = map(fnd, (a, b))
    if a != b:
        if a < b: pr[b] = a
        else: pr[a] = b
        rst += c
        v -= 1
print(rst)