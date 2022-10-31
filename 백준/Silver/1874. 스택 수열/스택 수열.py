t = int(input())
n = 1
rst = ''
st = []
for i in range(t):
    tg = int(input())
    while n <= tg :
        rst += '+'
        st.append(n)
        n += 1
    if tg == st[-1] : rst += '-'; st.pop();
    else : rst = 'NO'; break
if rst == 'NO' : print(rst)
else :
    for a in rst : print(a)