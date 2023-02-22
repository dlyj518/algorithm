n = int(input())
ls = []
for _ in range(n): ls.append(int(input()))
ls.sort()
for i in range(n): print(ls[i])