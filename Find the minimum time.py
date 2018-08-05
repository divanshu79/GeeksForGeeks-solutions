for _ in range(int(input())):
    x,y,z = map(int, input().split())
    a = 0
    diff = abs(x-y)
    if z%2 == 0:
        a = z//2
    else:
        a = z//2+1
    scanner_1 = x*a
    scanner_2 = y*a
    t_time = 0
    if abs(scanner_1-scanner_2) <= diff:
        t_time = min(scanner_1,scanner_2)
    else:
        while abs(scanner_1-scanner_2) > diff:
            1_ck = min(scanner_1,scanner_2)
            2_ck = 
