sk = input()
st = []
rst = ''
for s in sk:
    if s in ['+', '-']:
        while st and st[-1] != '(': rst += st.pop()
        st.append(s)
    elif s in ['*', '/']:
        while st and st[-1] in ['*', '/']: rst += st.pop()
        st.append(s)
    elif s == ')':
        while st[-1] != '(': rst += st.pop()
        st.pop()
    elif s == '(': st.append('(')
    else: rst += s
while st: rst += st.pop()
print(rst)