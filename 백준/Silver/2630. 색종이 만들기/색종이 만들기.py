def cntp(s1,s2,e1,e2):
    global clp, blp
    l = e1-s1
    x = [paper[i][s2:e2] for i in range(s1, e1)]
    s = sum(sum(x, []))
    if s == l**2: clp += 1; return
    if s == 0 : blp += 1; return
    else:
        m1,m2 = (s1+e1) // 2, (s2+e2) // 2
        cntp(s1,s2,m1,m2)
        cntp(s1,m2,m1,e2)
        cntp(m1,s2,e1,m2)
        cntp(m1,m2,e1,e2)

n = int(input())
paper = [list(map(int,input().split())) for _ in range(n)]
clp, blp = 0,0
cntp(0,0,n,n)
print(blp)
print(clp)