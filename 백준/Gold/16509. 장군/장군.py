from collections import deque

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
mp = [[100] * 9 for _ in range(10)]
ss = [[(0, -1), (-1, -1)], [(0, -1), (1, -1)],
      [(0, 1), (-1, 1)], [(0, 1), (1, 1)],
      [(-1, 0), (-1, 1)], [(-1, 0), (-1, -1)],
      [(1, 0), (1, 1)], [(1, 0), (1, -1)]]
q = deque([(r1, c1, 1)])
while q:
    r, c, t = q.popleft()
    for s in range(8):
        nr, nc = r, c
        for i in range(2):
            nr += ss[s][i][0]; nc += ss[s][i][1]
            if not (0 <= nr < 10 and 0 <= nc < 9) or (nr == r2 and nc == c2): break
        else:
            nr += ss[s][1][0]; nc += ss[s][1][1]
            if 0 <= nr < 10 and 0 <= nc < 9:
                if nr == r2 and nc == c2: print(t); quit()
                if mp[nr][nc] > t: mp[nr][nc] = t; q.append((nr, nc, t + 1))
else: print(-1)