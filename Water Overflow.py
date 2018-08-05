for _ in range(int(input())):
    n = int(input())
    x = int(input())
    y = int(input())

    arr = []
    for i in range(1,x+1):
        p = [0]*i
        arr.append(p)

    arr[0][0] = n

    for i in range(len(arr)-1):
        for j in range(len(arr[i])):
            if arr[i][j] > 1:
                arr[i+1][j] += (arr[i][j]-1)/2
                arr[i+1][j+1] += (arr[i][j]-1)/2
    if arr[x-1][y-1] >= 1:
        print("%.6f" % 1)
    else:
        print("%.6f" % arr[x - 1][y - 1])