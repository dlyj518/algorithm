import sys
input = sys.stdin.readline
sys.setrecursionlimit(600000)

def dfs(x, a):
    global r
    ch[x] = 0
    c = 1
    for i in tr[x]:
        if ch[i]: dfs(i, a + 1); c = 0
    if c: r += a

n = int(input())
tr = [[] for _ in range(n + 1)]
dp = [0] * (n + 1)
ch = [1] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    tr[a].append(b); tr[b].append(a)
r = 0
dfs(1, 0)
print('Yes') if r % 2 else print('No')