def pr(x, k):
    for i in range(x):
        if k == chk[i] or abs(k - chk[i]) == abs(x - i): return False
    return True

def nq(x):
    global rst
    if n == x: rst += 1; return
    for i in range(n):
        if pr(x, i): chk[x] = i; nq(x+1)

n = int(input())
chk, rst = [0]*n, 0
nq(0)
print(rst)