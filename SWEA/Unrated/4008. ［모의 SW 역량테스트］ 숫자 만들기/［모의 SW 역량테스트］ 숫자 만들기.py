def cal(x,y,i):
    if i == 0: return x + y
    if i == 1: return x - y
    if i == 2: return x * y
    return int(x / y)

def dfs(arr, x, i=0):
    if i == n-1: rst.append(x); return
    tmp = arr[:]
    for k in range(4):
        if arr[k] > 0:
            tmp[k] -= 1
            dfs(tmp, cal(x, num[i+1], k), i+1)
            tmp[k] += 1

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    ys = list(map(int, input().split()))
    num = list(map(int, input().split()))
    rst = []
    dfs(ys, num[0])
    print(f'#{tc} {max(rst)-min(rst)}')