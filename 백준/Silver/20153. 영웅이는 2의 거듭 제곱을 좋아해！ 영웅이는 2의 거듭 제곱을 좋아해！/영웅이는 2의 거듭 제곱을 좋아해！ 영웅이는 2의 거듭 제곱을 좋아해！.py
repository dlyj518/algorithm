n = int(input())
aa = list(map(int, input().split()))
s = 0
for a in aa: s ^= a
mx = max(s, max(s ^ a for a in aa))
print(f'{mx}{mx}')