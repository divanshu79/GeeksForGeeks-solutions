for _ in range(int(input())):
    n = int(input())
    x = int(input())
    y = int(input())

    arr = []
    for i in range(1,x+1):
        p = [0]*i
        arr.append(p)
    flag = 0
    for i in range(len(arr)):
        if n > 1:
            arr[i][0] = n-1
            n = n-1
            n = n//2
        else:
            arr[i][0] = n
            n = 0
            break
    if y > x//2:
        y = x-y+1
    p = 0
    if x%2 == 0:
        p = x//2
    else:
        p = x//2+1
    for i in range(1, p+1):
        pass