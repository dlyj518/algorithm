from itertools import combinations

n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
q = sorted(list(set(combinations(l, m))))
for a in q: print(*a)