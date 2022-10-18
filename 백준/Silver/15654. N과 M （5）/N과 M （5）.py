from itertools import permutations
n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
for i in permutations(l, m): print(*i)