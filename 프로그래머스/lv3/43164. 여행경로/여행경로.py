def solution(tickets):
    dt = {}
    n = len(tickets)
    for a, b in tickets:
        if dt.get(a,0) == 0: dt[a] = [b]
        else: dt[a].append(b)
    for a in dt: dt[a].sort()
    answer = dfs("ICN", ['ICN'], dt, n)
    return answer

def dfs(st, rst, dt, n):
    r = rst[:]
    if len(r) == n+1: return r
    if dt.get(st, 0) == 0: return
    for ed in dt[st]:
        dt[st].remove(ed)
        rs = dfs(ed, rst+[ed], dt, n)
        if rs != None: return rs
        dt[st].append(ed); dt[st].sort()