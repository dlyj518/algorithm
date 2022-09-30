def nq(n, i = 0, arr = []):
    global rst
    if n == i: rst += 1
    chk = arr[:]
    for c in range(len(chk)):
        nc = i-c
        if chk[c]+nc < n: chk.append(chk[c]+nc)
        if chk[c]-nc >= 0: chk.append(chk[c]-nc)
    for j in range(n):
        if j not in chk: nq(n, i+1, arr+[j])

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    rst = 0
    nq(n)
    print(f'#{tc} {rst}')