ab = [[0, 2, 1, 3], [0, 1, 3, 2], [0, 3, 2, 1]]
ls = list(input())
r = 1
for a in ls: r = ab[ord(a) - 65][r]
print(r)