for _ in range(int(input())):
    n, m = map(int, input().split())

    mat = []
    for i in range(n):
        k = []
        for j in range(m):
            k.append(0)
        mat.append(k)

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0:
                mat[i][j] = 1
            else:
                mat[i][j] = mat[i-1][j] + mat[i][j-1]
    print(mat[n-1][m-1])