from bisect import bisect_left
n = int(input())
ls = list(map(int, input().split()))
dpu, dpd = [0]*n, [0]*n
eju, ejd = [-1e11], [-1e11]
for i in range(n):
    if ls[i] > eju[-1]: eju.append(ls[i]); dpu[i] = len(eju)-1
    else: dpu[i] = bisect_left(eju, ls[i]); eju[dpu[i]] = ls[i]
    if ls[n-i-1] > ejd[-1]: ejd.append(ls[n-i-1]); dpd[n-i-1] = len(ejd)-1
    else: dpd[n-i-1] = bisect_left(ejd, ls[n-i-1]); ejd[dpd[n-i-1]] = ls[n-i-1]
mx = 0
for i in range(n):
    if mx < dpu[i]+dpd[i]-1: mx = dpu[i]+dpd[i]-1
print(mx)