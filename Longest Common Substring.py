from collections import defaultdict
for _ in range(int(input())):
    n, m = map(int, input().split())
    str_1 = input()
    str_2 = input()
    def_dect = defaultdict(int)
    mat = []

    for i in range(n+1):
        k = []
        for j in range(m+1):
            k.append(0)
        mat.append(k)

    ans_max = 0
    for i in range(n+1):
        for j in range(m+1):
            if i != 0 and j != 0:
                if str_1[i-1] == str_2[j-1]:
                    mat[i][j] = mat[i-1][j-1] + 1
                    if mat[i][j] > ans_max:
                        ans_max = mat[i][j]
    print(ans_max)