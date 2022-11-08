from itertools import combinations_with_replacement

n, m = map(int, input().split())
l = sorted(list(set(map(int, input().split()))))
for a in combinations_with_replacement(l, m): print(*a)