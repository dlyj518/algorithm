n = int(input())
if n == 0: print(1)
else:
    rst = 1
    while n > 0:
        rst *= n
        n -= 1
    print(rst)