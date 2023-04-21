import sys
input = sys.stdin.readline
n = int(input())
tr = [[] for _ in range(n + 1)]
for i in range(1, n + 1): tr[i] = list(map(int, input().split()))
k = int(input())
r = 1
while 1:
    if sum(tr[r]) == -2: print(r); break
    if tr[r][0] == -1: r = tr[r][1]
    elif tr[r][1] == -1: r = tr[r][0]
    elif k % 2: r = tr[r][0]; k = k // 2 + 1
    else: r = tr[r][1]; k //= 2