from itertools import combinations
n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
for a in combinations(l, m): print(*a)