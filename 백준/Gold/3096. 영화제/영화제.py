from itertools import combinations as cb
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rd = {i: set() for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    rd[a].add(b)
rst = 0
for a, b in list(cb(range(1, n+1), 2)):
    lrd = len(rd[a] & rd[b])
    if lrd > 1: rst += (lrd * (lrd - 1)) // 2
print(rst)