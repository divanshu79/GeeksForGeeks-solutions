for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    pre_ans = 0
    pre = 0
    for i in arr:
        if i == 0:
            pre_ans += 1
            pre = i
        else:
            if pre+1 == i:
                pre = i
                pre_ans += 1
            else:
                if pre_ans > ans:
                    ans = pre_ans
                pre = i
                pre_ans = 1
    if pre_ans > ans:
        print(pre_ans)
    else:
        print(ans)