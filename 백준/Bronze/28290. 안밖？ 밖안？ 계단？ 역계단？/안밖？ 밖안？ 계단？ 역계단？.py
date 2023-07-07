x = input()
if x[:4] == 'asdf':
    if x[4:8] == 'jkl;': print('stairs')
    elif x[4:8] == ';lkj': print('out-in')
    else: print('molu')
elif (x[:4] == 'jkl;' and x[4:8] == 'fdsa') or (x[:4] == 'fdsa' and x[4:8] == 'jkl;'): print('in-out')
elif x[:4] == ';lkj':
    if x[4:8] == 'fdsa': print('reverse')
    elif x[4:8] == 'asdf': print('out-in')
    else: print('molu')
else: print('molu')    