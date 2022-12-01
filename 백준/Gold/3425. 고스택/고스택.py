def calc(mr, n):
    st = [n]
    for m in mr:
        if m[:3] == 'NUM': st.append(int(m[4:]))
        elif not st: return 'ERROR'
        elif m == 'POP': st.pop()
        elif m == 'INV': st[-1] = -st[-1]
        elif m == 'DUP': st.append(st[-1])
        elif len(st) < 2: return 'ERROR'
        elif m == 'SWP': st[-1], st[-2] = st[-2], st[-1]
        else:
            x, y = st.pop(), st.pop()
            if m == 'ADD' and abs(x+y) <= 1e9: st.append(x + y)
            elif m == 'SUB' and abs(y-x) <= 1e9: st.append(y - x)
            elif m == 'MUL' and abs(x*y) <= 1e9: st.append(x * y)
            elif x == 0: return 'ERROR'
            elif m == 'DIV':
                if (x > 0) == (y > 0): st.append(abs(y) // abs(x))
                else: st.append(-(abs(y) // abs(x)))
            elif m == 'MOD':
                if y > 0: st.append(abs(y) % abs(x))
                else: st.append(-(abs(y) % abs(x)))
            else: return 'ERROR'
    if len(st) != 1: return 'ERROR'
    else: return st[0]

while 1:
    mr = []
    while 1:
        a = input()
        if a == 'QUIT': quit()
        if a == 'END': break
        mr.append(a)
    n = int(input())
    for _ in range(n): print(calc(mr, int(input())))
    input()
    print()