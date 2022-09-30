import sys
input = sys.stdin.readline
import heapq

t = int(input())
for _ in range(t):
    k = int(input())
    mnhp,mxhp = [], []
    vs = [0]*1000001
    for i in range(k):
        q,n = input().split()
        if q == 'I':
            heapq.heappush(mnhp, (int(n), i))
            heapq.heappush(mxhp, (-int(n), i))
        elif n == '1':
            while mxhp and vs[mxhp[0][1]] == 1: heapq.heappop(mxhp)
            if mxhp: vs[mxhp[0][1]] = 1; heapq.heappop(mxhp)
        else:
            while mnhp and vs[mnhp[0][1]] == 1: heapq.heappop(mnhp)
            if mnhp: vs[mnhp[0][1]] = 1; heapq.heappop(mnhp)
    while mnhp and vs[mnhp[0][1]] == 1: heapq.heappop(mnhp)
    while mxhp and vs[mxhp[0][1]] == 1: heapq.heappop(mxhp)
    if mnhp and mxhp: print(f'{-mxhp[0][0]} {mnhp[0][0]}')
    else: print('EMPTY')