x = list(input())
p = list(input())
n = len(p)
st = []
for a in x:
    st.append(a)
    if len(st) >= n and st[-n:] == p:
        for i in range(n): st.pop()
if len(st) == 0: print('FRULA')
else:
    for i in st: print(i, end='')