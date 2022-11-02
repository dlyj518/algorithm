import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def pr(si, ei, sp, ep):
    global rst
    if si > ei or sp > ep: return
    nd = ps[ep]
    print(nd, end=' ')
    i = pp[nd]
    pr(si, i-1, sp, sp+(i-si)-1)
    pr(i+1, ei, ep-ei+i, ep-1)

n = int(input())
io = list(map(int, input().split()))
ps = list(map(int, input().split()))
pp = [0]*(n+1)
for i in range(n): pp[io[i]] = i
pr(0, n-1, 0, n-1)