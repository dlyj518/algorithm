import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pr = [[] for _ in range(n + 1)]
ch = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    pr[b].append(a); ch[a].append(b)
st = []; rst = []
while 1:
    for i in range(1, n+1):
        if not pr[i]: st.append(i)
    if not st: break
    while st:
        j = st.pop()
        for k in ch[j]: pr[k].remove(j)
        rst.append(j)
        pr[j] = [-1]
print(*rst)