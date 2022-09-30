import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().split()))
k, ss = 0, [0]
for i in range(n):
    k += s[i]
    ss.append(k)
for _ in range(m):
    a, b = map(int, input().split())
    print(ss[b] - ss[a-1])