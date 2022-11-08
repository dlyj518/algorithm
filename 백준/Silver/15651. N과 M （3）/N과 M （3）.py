from itertools import product

n, m = map(int, input().split())
l = [i+1 for i in range(n)]
for a in product(l, repeat=m): print(*a)