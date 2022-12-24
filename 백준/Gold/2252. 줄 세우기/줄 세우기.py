import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pr = [0]*(n + 1)
ch = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    pr[b] += 1; ch[a].append(b)
st = []; rst = []
for i in range(1, n+1):
    if not pr[i]: st.append(i)
while st:
    j = st.pop()
    for k in ch[j]:
        pr[k] -= 1
        if not pr[k]: st.append(k)
    rst.append(j)
print(*rst)