n = int(input())
ip =[list(map(int, input().split('.'))) for _ in range(n)]
l = 4
for a in range(1, n):
    for i in range(l):
        if ip[0][i] != ip[a][i]: l = i; break
if l == 4: print(32)
else:
    x = 0
    for i in range(n - 1):
        x = max((ip[i][l] ^ ip[i + 1][l]).bit_length() - 1, x)
    print(l * 8 + (7 - x))