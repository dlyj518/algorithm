def pwr(adj, n):
    if n == 1: return adj
    if n%2: return ag(pwr(adj, n-1), adj)
    return pwr(ag(adj, adj), n//2)

def ag(a, b):
    rst = [[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            s = 0
            for k in range(2): s += a[i][k]*b[k][j]
            rst[i][j] = s%1000000
    return rst
n = int(input())
adj = [[1, 1], [1, 0]]
st = [[1],[1]]
if n == 0: print(0)
elif n < 3: print(1)
else: print(ag(pwr(adj, n-2), st)[0][0])