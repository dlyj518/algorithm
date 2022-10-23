import sys
input = sys.stdin.readline

n, m = map(int, input().split())

mp = [list(map(int, input().split())) for _ in range(n)]
sm = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        sm[i][j] = sm[i][j-1] + sm[i-1][j] + mp[i-1][j-1] - sm[i-1][j-1]
for _ in range(m):
    a, b, c, d = map(int, input().split())
    print(sm[c][d] - sm[c][b-1] - sm[a-1][d] + sm[a-1][b-1])