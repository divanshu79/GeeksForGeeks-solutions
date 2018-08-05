for _ in range(int(input())):
    n, m = map(int, input().split())
    string_1, string_2 = map(str, input().split())
    a = []
    for i in range(n+1):
        k = []
        for j in range(m+1):
            k.append(0)
        a.append(k)

    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                a[i][j] = j
            elif j == 0:
                a[i][j] = i
            elif string_1[i-1] == string_2[j-1]:
                a[i][j] = a[i-1][j-1]
            else:
                a[i][j] = 1 + min(a[i-1][j], a[i-1][j-1], a[i][j-1])
    print(a[n][m])