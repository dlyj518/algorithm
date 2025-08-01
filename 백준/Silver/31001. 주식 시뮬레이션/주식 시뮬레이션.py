n, m, q = map(int, input().split())
grp = {}
cpn = {}
js = {}
for _ in range(n):
    g, h, p = input().split()
    p = int(p)
    if grp.get(g, 0): grp[g].append(h)
    else: grp[g] = [h]
    cpn[h] = p
    js[h] = 0
for _ in range(q):
    inp = list(input().split())
    if inp[0] == '1' and cpn[inp[1]] * int(inp[2]) <= m:
        js[inp[1]] += int(inp[2])
        m -= cpn[inp[1]] * int(inp[2])
    elif inp[0] == '2' and js[inp[1]]:
        p = min(js[inp[1]], int(inp[2]))
        js[inp[1]] -= p
        m += cpn[inp[1]] * p
    elif inp[0] == '3': cpn[inp[1]] += int(inp[2])
    elif inp[0] == '4':
        for g in grp[inp[1]]: cpn[g] += int(inp[2])
    elif inp[0] == '5':
        for g in grp[inp[1]]: cpn[g] = int((cpn[g] * (100 + int(inp[2]))) / 1000) * 10
    elif inp[0] == '6': print(m)
    elif inp[0] == '7':
        s = m
        for c in js: s += cpn[c] * js[c]
        print(s)