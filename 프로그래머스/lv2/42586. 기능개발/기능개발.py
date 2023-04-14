def solution(progresses, speeds):
    answer = []
    rs = [0] * len(speeds)
    for i in range(len(progresses)):
        while progresses[i] < 100:
            rs[i] += 1
            progresses[i] += speeds[i]
    c = 0
    t = rs[0]
    for r in rs:
        if r > t:
            t = r
            answer.append(c)
            c = 1
        else: c += 1
    answer.append(c)
    return answer