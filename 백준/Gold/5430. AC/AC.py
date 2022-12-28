from collections import deque

t = int(input())
for tc in range(t):
    p = input()
    n = int(input())
    x = deque(input()[1:-1].split(','))
    if n == 0 : x = deque()
    chk = 0
    rn = 0
    for a in p:
        if a == 'R': rn += 1
        if a == 'D':
            if not x:print('error');chk = 1;break
            else:
                if rn%2 == 0: x.popleft()
                else: x.pop()
    if chk == 1: continue
    if rn%2 == 1: x.reverse()
    print(f'[{",".join(x)}]')