import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,n=0):
    global cnt
    vs[x] = 1
    chk = 1
    for a in eg[x]:
        if not vs[a]: chk = 0; dfs(a,n+1)
    if chk == 1: cnt += n

n = int(input())
vs = [0]*(n+1)
eg = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    eg[a].append(b)
    eg[b].append(a)
cnt = 0
dfs(1)
yn = 'No' if cnt % 2 == 0 else 'Yes'
print(yn)