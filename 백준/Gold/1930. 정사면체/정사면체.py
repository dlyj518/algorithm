t = [[0, 1, 2, 3], [1, 0, 3, 2], [2, 0, 1, 3], [3, 0, 2, 1]]
n = int(input())
for _ in range(n):
    ls = list(map(int, input().split()))
    a, b = ls[:4], ls[4:]
    q = 0
    for i in range(4):
        c = [b[t[i][0]], b[t[i][1]], b[t[i][2]], b[t[i][3]]]
        for j in range(3):
            c[1:] = [c[3]] + c[1:3]
            if a == c: print(1); q = 1; break
        if q: break
    else: print(0)