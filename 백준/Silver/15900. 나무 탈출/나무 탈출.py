import sys
input = sys.stdin.readline

n = int(input())
tr = [[] for _ in range(n + 1)]
ch = [1] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    tr[a].append(b); tr[b].append(a)
r = 0
st = [(1, 0)]
while st:
    x, y = st.pop(-1)
    ch[x] = 0
    c = 1
    for i in tr[x]:
        if ch[i]: st.append((i, y + 1)); c = 0
    if c: r += y
print('Yes') if r % 2 else print('No')