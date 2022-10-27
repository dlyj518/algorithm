n, m = map(int, input().split())
gs = []
for _ in range(m):
    s, e, t = map(int, input().split())
    gs.append([s, e, t])
sr = [0]*2+[1e9]*(n-1)
imp = 0
for a in range(n):
    for s, e, t in gs:
        if sr[s] != 1e9 and sr[e] > sr[s]+t:
            sr[e] = sr[s]+t
            if a == n-1: imp = 1
if imp: print(-1)
else:
    for i in range(2, n+1):
        if sr[i] == 1e9: print(-1)
        else: print(sr[i])