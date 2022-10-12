def solution(n, results):
    w = [set() for _ in range(n+1)]
    l = [set() for _ in range(n+1)]
    for a, b in results:
        w[a].add(b); l[b].add(a)
    for i in range(1, n+1):
        for ww in w[i]: l[ww].update(l[i])
        for ll in l[i]: w[ll].update(w[i])
    answer = 0
    for i in range(1, n+1):
        if len(w[i])+len(l[i]) == n-1: answer += 1
    return answer