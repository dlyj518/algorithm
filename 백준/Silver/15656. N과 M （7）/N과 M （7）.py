from itertools import product

n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
for a in product(l, repeat=m): print(*a)