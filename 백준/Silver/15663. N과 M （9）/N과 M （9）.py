from itertools import permutations
from collections import deque
n, m = map(int, input().split())
l = list(map(int, input().split()))
q = sorted(list(set(permutations(l, m))))
for a in q: print(*a)