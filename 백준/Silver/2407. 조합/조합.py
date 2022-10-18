n, r = map(int, input().split())
f = [0, 1]
for i in range(1, n): f.append(f[i]*(i+1))
print(f[n]//(f[n-r]*f[r]))