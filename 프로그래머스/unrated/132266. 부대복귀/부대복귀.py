from heapq import *

def solution(n, roads, sources, destination):
    answer = []
    rd = [[] for _ in range(n+1)]
    for i, j in roads: rd[i].append(j); rd[j].append(i)
    d = [n+1]*(n+1)
    d[destination] = 0
    q = [(destination, 0)]
    while q:
        m, c = heappop(q)
        for a in rd[m]:
            if d[a] > c + 1: d[a] = c + 1; heappush(q, (a, c + 1))
    for s in sources:
        if d[s] == n+1: answer.append(-1)
        else: answer.append(d[s])
    return answer