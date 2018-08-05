for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = []

    for i in range(a):
        mid_ans = []
        for j in range(b):
            if i == 0 or j == 0:
                mid_ans.append(1)
            else:
                try:
                    mid_ans.append(ans[j][i])
                except:
                    k = mid_ans[len(mid_ans)-1]+ans[i-1][j]
                    mid_ans.append(k)
        ans.append(mid_ans)
    print(ans[a-1][b-1])
