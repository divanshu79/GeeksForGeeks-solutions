for _ in range(int(input())):
    egg, floor = map(int, input().split())
    ans = []

    for i in range(egg):
        mid_ans = []
        for j in range(floor):
            if i == 0:
                mid_ans.append(j+1)
            elif j == 0:
                mid_ans.append(1)
            else:
                k = 1000000
                fl = j
                while fl != 0:
                    s = 0
                    if fl == j:
                        s = 1 + max(ans[i-1][j-1], 0)
                    elif fl == 0:
                        s = 1 + max(0, mid_ans[j-1])
                    else:
                        s = 1 + max(ans[i-1][fl-1], mid_ans[j-fl-1])
                    if s < k:
                        k = s
                    fl -= 1
                mid_ans.append(k)
        ans.append(mid_ans)
    print(ans[egg-1][floor-1])
