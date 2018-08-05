a = list(map(int, input().split()))
b = list(map(int, input().split()))
if len(a) == 1:
    print(0)
else:
    n, arr_1 = a[0], a[1:]
    m, arr_2 = b[0], b[1:]

    mat = []
    for i in range(n):
        mat.append((arr_1[i], arr_2[i]))
    steps = 0
    for i in range(0, n-1):
        fr = mat[i]
        se = mat[i+1]
        k = abs(fr[0] - se[0])
        p = abs(fr[1]-se[1]) - k
        pp = k + p
        steps += pp
    print(steps)