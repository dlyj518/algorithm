def solution(clothes):
    dt = {}
    for c, t in clothes:
        if dt.get(t, 0) == 0: dt[t] = 1
        else: dt[t] += 1
    num = list(dt.values())
    answer = 1
    for i in num:
        answer *= 1+i
    return answer - 1