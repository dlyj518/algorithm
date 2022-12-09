import sys
input = sys.stdin.readline
n = int(input())
lg = {}
for _ in range(n):
    l, m = input().split()
    if m == 'enter': lg[l] = 1
    else: del(lg[l])
print(*sorted(lg, reverse=True), sep='\n')