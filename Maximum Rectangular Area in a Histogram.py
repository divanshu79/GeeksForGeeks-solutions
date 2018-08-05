for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    max_ans = 0
    check_ans = 0
    tot_ind = 0
    min_val = 0

    for i in arr:
        tot_ind += 1
        if min_val == 0:
            min_val = i
        else:
            if i < min_val:
                min_val = i
        check_ans = min_val*tot_ind
        if check_ans > max_ans:
            pass