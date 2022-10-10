def ys(a, b, y):
    if y == '+': return a+b
    if y == '-': return a-b
    return a*b

def gh(i, x):
    global mx, n
    if i >= n:
        if x > mx: mx = x
        return
    gh(i+2, ys(x, s[i + 1], s[i]))
    if i >= n-2: return
    gh(i+4, ys(x, ys(s[i+1], s[i+3], s[i+2]), s[i]))

n = int(input())
s = [int(x) if x != "+" and x != "-" and x != "*" else x for x in input().strip()]
mx = -2**31
gh(1, s[0])
print(mx)