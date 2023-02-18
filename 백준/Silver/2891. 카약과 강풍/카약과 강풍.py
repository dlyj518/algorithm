n, s, r = map(int, input().split())
ss = list(map(int, input().split()))
rr = list(map(int, input().split()))
ls = [0] * (n + 1)
for i in ss: ls[i] = 1
for i in rr:
    if ls[i]: ls[i] = 0
    elif ls[i - 1]: ls[i - 1] = 0
    elif i < n and ls[i + 1]: ls[i + 1] = 0
print(sum(ls))