import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def fdt(x, l):
    global rs
    if vs[x]: return
    vs[x] = 1
    x = pr[x]
    if vs[x]:
        if x in l:
            rs -= len(l) - l.index(x)
    else: l.append(x); fdt(x, l)


t = int(input())
for _ in range(t):
    n = int(input())
    pr = [0] + list(map(int, input().split()))
    vs = [0] * (n + 1)
    rs = n
    for i in range(1, n + 1): fdt(i, [i])
    print(rs)
