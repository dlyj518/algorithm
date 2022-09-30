s = [0,1,2,4]
for i in range(4,12):
    s.append(sum(s[i-3:i]))
for _ in range(int(input())):
    print(s[int(input())])
