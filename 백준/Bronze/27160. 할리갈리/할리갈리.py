import sys
input = sys.stdin.readline

n = int(input())
fr = {'STRAWBERRY': 0, 'BANANA': 0, 'LIME': 0, 'PLUM': 0}
for _ in range(n):
    f, i = input().split()
    fr[f] += int(i)
for f in fr:
    if fr[f] == 5: print('YES'); break
else: print('NO')