while 1:
    a = input()
    if a == '#': break
    s = 0
    for i in a:
        if i.upper() in ['A','E','I','O','U']: s += 1
    print(s)