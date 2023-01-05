x = list(input())
p = list(input())
n = len(p)
st = []
for a in x:
    st.append(a)
    if st[-n:] == p:
        for i in range(n): st.pop()
if len(st) == 0: print('FRULA')
else: print(''.join(st))