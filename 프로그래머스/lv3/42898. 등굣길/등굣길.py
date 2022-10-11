def solution(m, n, puddles):
    mp = [[0]*(m+1) for _ in range(n+1)]
    mp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j == 1: continue
            if [j, i] in puddles: mp[i][j] = 0
            else: mp[i][j] = mp[i-1][j] + mp[i][j-1]
    answer = mp[n][m] % 1000000007
    return answer