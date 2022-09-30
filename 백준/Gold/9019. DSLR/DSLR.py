import sys
input = sys.stdin.readline
from collections import deque

def bfs(s,e):
    vs = set()
    vs.add(s)
    q = deque([(s, '')])
    while q:
        x, m = q.popleft()
        if x == e: return m
        c = (x * 2) % 10000
        if not c in vs: vs.add(c); q.append((c, m + 'D'))
        c = (x - 1) % 10000
        if not c in vs: vs.add(c); q.append((c, m + 'S'))
        c = (x // 1000) + x % 1000 * 10
        if not c in vs: vs.add(c); q.append((c, m + 'L'))
        c = x // 10 + (x % 10) * 1000
        if not c in vs: vs.add(c); q.append((c, m + 'R'))

n = int(input())
for _ in range(n):
    bf, af = map(int, input().split())
    print(bfs(bf,af))