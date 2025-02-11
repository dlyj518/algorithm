def rec(s, l, r, c):
    if l >= r: return [1, c]
    if s[l] != s[r]: return [0, c]
    return rec(s, l + 1, r - 1, c + 1)

def isp(s): return rec(s, 0, len(s) - 1, 1)

for i in range(int(input())): print(*isp(input()))