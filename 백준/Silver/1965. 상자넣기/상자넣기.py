n = int(input())
x = list(map(int,input().split()))
c = [0,x[0]]
m = 1
for i in range(1,n):
    if c[m] < x[i]:
        m += 1
        c.append(x[i])
    else:
        for j in range(m+1):
            if c[j] >= x[i]:
                c[j] = x[i]
                break
print(m)