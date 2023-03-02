n, l = map(int, input().split())
mp = []
r = 0
for i in range(n):
    mp.append(list(map(int, input().split())))
    c = p = 1
    for j in range(n):
        if (j != 0 and p > 0):
            if mp[i][j] == mp[i][j - 1]: c += 1
            elif mp[i][j] - 1 == mp[i][j - 1]:
                if c < l: p = 0; continue
                c = 1
            elif mp[i][j] + 1 == mp[i][j - 1]:
                if c < 0: p = 0; continue
                c = - l + 1
            else: p = 0
    if p > 0 and c >= 0: r += 1
for i in range(n):
    c = p = 1
    for j in range(n):
        if (j != 0 and p > 0):
            if mp[j][i] == mp[j - 1][i]: c += 1
            elif mp[j][i] - 1 == mp[j - 1][i]:
                if c < l: p = 0; continue
                c = 1
            elif mp[j][i] + 1 == mp[j - 1][i]:
                if c < 0: p = 0; continue
                c = - l + 1
            else: p = 0
    if p > 0 and c >= 0: r += 1
print(r)