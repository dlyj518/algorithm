from itertools import product
n, m = map(int, input().split())
l = list(set(map(int, input().split())))
q = sorted(list(set(product(l, repeat=m))))
for a in q: print(*a)