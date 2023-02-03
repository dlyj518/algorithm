st, ed = [9], [18]
while max(st[-1], ed[-1]) < 4294967295:
    st.append(st[-1] * 18)
    ed.append(ed[-1] * 18)
while 1:
    try: n = int(input())
    except: break
    i = 0
    while ed[i] < n: i += 1
    print ('Donghyuk wins.') if n > st[i] else print ('Baekjoon wins.') 