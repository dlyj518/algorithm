a, b = map(int, input().split())
x = a * b
ls = list(map(int, input().split()))
l = []
for i in ls: print(i - x, end=' ')