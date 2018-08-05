for _ in range(int(input())):
    n = input()
    flag = 0
    try:
        n = int(n)
    except:
        flag = 1
    if flag == 0:
        print(n)
    else:
        print(-1)