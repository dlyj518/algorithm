import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def pst(ls):
    n = len(ls)
    if n <= 1: return ls
    for i in range(1, n):
        if ls[i] > ls[0]: return pst(ls[1:i]) + pst(ls[i:]) + [ls[0]]
    return pst(ls[1:]) + [ls[0]]

nm = []
while 1:
    try: nm.append(int(input()))
    except: break

for i in pst(nm): print(i)