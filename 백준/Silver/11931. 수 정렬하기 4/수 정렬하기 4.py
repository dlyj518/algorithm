import sys
input = sys.stdin.readline
ls = []
for i in range(int(input())): ls.append(int(input()))
ls.sort()
for i in range(len(ls)): print(ls[-1 - i])