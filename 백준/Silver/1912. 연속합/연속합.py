n = int(input())
ls = list(map(int, input().split()))
mx = [-1e8]
for x in ls: mx.append(max(mx[-1] + x, x))
print(max(mx))