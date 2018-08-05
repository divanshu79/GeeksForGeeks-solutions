for _ in range(int(input())):
    m, n = map(int, input().split())
    str_1 = input()
    str_2 = input()

    mat = []
    for i in range(m+1):
        k = [0]*(n+1)
        mat.append(k)
    ans = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if str_1[i-1] == str_2[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
            else:
                mat[i][j] = max(mat[i-1][j], mat[i][j-1])

            if mat[i][j] > ans:
                ans = mat[i][j]
    print(ans)