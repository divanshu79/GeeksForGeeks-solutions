for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    ans_list = ''
    pre_ans_list = ''
    max_score = 0
    pre_max_score = 0

    for i in range(n):
        if arr[i] < 0:
            if max_score > pre_max_score:
                pre_max_score = max_score
                pre_ans_list = ans_list
            elif max_score == pre_max_score:
                if len(ans_list) > len(pre_ans_list):
                    pre_ans_list = ans_list
                    pre_max_score = max_score
            ans_list = ''
            max_score = 0
        else:
            max_score += arr[i]
            ans_list += str(arr[i]) + " "
    if max_score > pre_max_score:
        print(ans_list)
    elif max_score == pre_max_score:
        if len(ans_list) > len(pre_ans_list):
            print(ans_list)
        else:
            print(pre_ans_list)
    else:
        print(pre_ans_list)