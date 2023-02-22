import sys
x = []
for i in range(int(input())): x.append(int(sys.stdin.readline()))
x.sort(reverse=True)
for i in x: print(i)