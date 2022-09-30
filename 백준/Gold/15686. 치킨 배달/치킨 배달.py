def dst(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1])

def ckds(arr):
    cnt = [n*2]*len(hs)
    for c in arr:
        for i in range(len(hs)):
            cnt[i] = min(cnt[i], dst(c, hs[i]))
    return sum(cnt)

def nck(n, k, x, arr=[]):
    arr = arr[:]
    if k == 0: rst.append(ckds(arr)); return
    for i in range(k-1, n):
        arr.append(x[i])
        nck(i, k-1, x, arr)
        arr.remove(x[i])


n, m = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
hs, ck = [], []
for i in range(n):
    for j in range(n):
        if mp[i][j] == 1: hs.append([i, j])
        if mp[i][j] == 2: ck.append([i, j])
rst = []
nck(len(ck), m, ck)
print(min(rst))