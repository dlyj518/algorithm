b = list(map(int, input().split()))
dp = [0] * b[0] + [1]
mx = 2
for i in range(b[0] + 1, 501):
    st = [1] * mx
    for l in b:
        if i >= l: st[dp[i - l]] = 0
    for j in range(mx):
        if st[j]: dp.append(j); break
    else: dp.append(mx); mx += 1
for _ in range(5):
    k, l = map(int, input().split())
    print('A') if dp[k] ^ dp[l] else print('B')