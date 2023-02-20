def pow(n):
    if n == 1: return mt
    mp = pow(n // 2)
    if n % 2: return mtm(mtm(mp, mp), mt)
    else: return mtm(mp, mp)
def mtm(a, b):
    return [[sum(a[i][k] * b[k][j]for k in range(8)) % 1000000007
           for j in range(8)] for i in range(8)]

mt = [[0, 1, 1, 0, 0, 0, 0, 0],
      [1, 0, 1, 1, 0, 0, 0, 0],
      [1, 1, 0, 1, 1, 0, 0, 0],
      [0, 1, 1, 0, 1, 1, 0, 0],
      [0, 0, 1, 1, 0, 1, 0, 1],
      [0, 0, 0, 1, 1, 0, 1, 0],
      [0, 0, 0, 0, 0, 1, 0, 1],
      [0, 0, 0, 0, 1, 0, 1, 0]]
n = int(input())
rs = pow(n)
print(rs[0][0])