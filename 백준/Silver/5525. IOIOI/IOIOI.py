n = int(input())
m = int(input())
s = input()
cnt = 0
i = 0
k = 0
while i < m-2:
    if s[i:i+3] == 'IOI':
        k += 1
        if k == n: cnt += 1; k -= 1
        i += 2
    else: i += 1; k = 0
print(cnt)