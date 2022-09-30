def chk(x, n):
    for i in range(len(x)):
        c = '1' if x[i] == '0' else '0'
        m = '0b' + x[:i] + c + x[i+1:]
        t, y = int(m,2), ''
        while t >= 3:
            y = str(t%3) + y
            t //= 3
        y = '0'*(n-len(y)-1) + str(t) + y
        cht.append(y)

t = int(input())
for tc in range(1,t+1):
    ntw = input()
    nth = input()
    cht = []
    chk(ntw, len(nth))
    c, zt = 0, ['0', '1', '2']
    for i in range(len(nth)):
        for x in zt:
            if nth[i] == x: continue
            m = nth[:i] + x + nth[i + 1:]
            if m in cht: c = 1; break
        if c == 1: break
    rst = 0
    for i in range(len(m)):
        rst += int(m[i])*3**(len(m)-i-1)
    print(f'#{tc} {rst}')