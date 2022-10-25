def ino(a='A'):
    global rst
    rst += a
    for i in tr[a]:
        if i != '.': ino(i)
def jw(a='A'):
    global rst
    if tr[a][0] != '.': jw(tr[a][0])
    rst += a
    if tr[a][1] != '.': jw(tr[a][1])
def hw(a='A'):
    global rst
    for i in tr[a]:
        if i != '.': hw(i)
    rst += a

n = int(input())
rst = ''
tr = {}
for i in range(1, n+1):
    a, b, c = input().split()
    tr[a] = [b, c]
ino()
rst += '\n'
jw()
rst += '\n'
hw()
print(rst)