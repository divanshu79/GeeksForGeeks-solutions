for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    mat = []
    pp = 0
    for i in range(n+2):
        k = []
        for j in range(m+2):
            if i == 0 or i == n+1:
                k.append(0)
            elif j == 0 or j == m+1:
                k.append(0)
            else:
                k.append(arr[pp])
                pp += 1
        mat.append(k)
    ans_list = []
    count = 0
    for i in range(n+2):
        for j in range(m+2):
            if mat[i][j] == 1:
                for x in range(-1,2,1):
                    for y in range(-1,2,1):
                        if x == 0 and y == 0:
                            pass
                        else:
                            if mat[i+x][j+y] == 1:
                                ans_list.append((i+x, j+y))
                                mat[i + x][j + y] = 0
                if len(ans_list) > 0:
                    while len(ans_list) != 0:
                        ii, jj = ans_list[0]
                        ans_list.pop(0)
                        for x in range(-1, 2, 1):
                            for y in range(-1, 2, 1):
                                if x == 0 and y == 0:
                                    pass
                                else:
                                    if mat[ii + x][jj + y] == 1:
                                        ans_list.append((ii + x, jj + y))
                                        mat[ii + x][jj + y] = 0
                count += 1
    print(count)
