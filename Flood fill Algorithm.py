for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    x, y, k = map(int, input().split())
    mat = []
    ind = 0
    for i in range(n+2):
        mm =  []
        for j in range(m+2):
            if i == 0 or j == 0 or i == n+1 or j == m+1:
                mm.append(-1000)
            else:
                mm.append(arr[ind])
                ind += 1
        mat.append(mm)
    check = mat[x+1][y+1]
    ans = ''
    check_list = [(x+1, y+1)]
    while len(check_list) > 0:
        g, h = check_list[0]
        check_list.pop(0)
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if abs(i) != abs(j):
                    if mat[g+i][h+j] == check:
                        mat[g+i][h+j] = k
                        check_list.append((g+i, h+j))
    mat[x+1][y+1] = k

    for i in range(n+2):
        for j in range(m+2):
            if i == 0 or j == 0 or i == n + 1 or j == m + 1:
                pass
            else:
                ans += str(mat[i][j]) + " "
    print(ans)