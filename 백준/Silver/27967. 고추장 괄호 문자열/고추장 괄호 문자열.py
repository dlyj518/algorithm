n = int(input())
a = input()

def chk(i, x, t):
    if x < 0: return ''
    if i == n:
        if not x: return t
        return ''
    if a[i] == '(': return chk(i + 1, x + 1, t + '(')
    if a[i] == ')': return chk(i + 1, x - 1, t + ')')
    r = chk(i + 1, x + 1, t + '(')
    if r: return r
    return chk(i + 1, x - 1, t + ')')
print(chk(0, 0, ''))