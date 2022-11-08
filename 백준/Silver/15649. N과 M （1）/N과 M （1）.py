from itertools import permutations
n, m = map(int, input().split())
l = [i+1 for i in range(n)]
for a in permutations(l, m): print(*a)