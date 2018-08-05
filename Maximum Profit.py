for _ in range(int(input())):
    k = int(input())
    n = int(input())
    arr = list(map(int, input().split()))

    buy_prise = 0
    profit = 0
    re_term = 0

    # for i in range(n):
    #     if i == 0:
    #         buy_prise = arr[i]
    #     else:
    #         if k-1 > 0:
    #             if arr[i] < arr[i-1]:
    #                 if arr[i-1] != buy_prise:
    #                     profit += re_term - buy_prise
    #                 buy_prise = arr[i]
    #                 re_term = 0
    #                 k -= 1
    #             elif arr[i] > arr[i - 1]:
    #                 if re_term < arr[i]:
    #                     re_term = arr[i]
    #         elif arr[i] > arr[i-1]:
    #             if re_term < arr[i]:
    #                 re_term = arr[i]
    # profit += re_term - buy_prise
    # if profit > 0:
    #     print(profit)
    # else:
    #     print(0)
    sort_arr = sorted(arr)
    sort_arr = sort_arr[:k]
    for i in range(n):
        if arr[i] in sort_arr:
            if buy_prise == 0:
                try:
                    if arr[i+1] not in sort_arr or arr[i+1] > arr[i]:
                        buy_prise = arr[i]
                    elif arr[i-1] not in sort_arr or arr[i-1] > arr[i]:
                        buy_prise = arr[i]
                except:
                    pass
            else:
                try:
                    if arr[i+1] not in sort_arr or arr[i+1] > arr[i]:
                        profit += re_term - buy_prise
                        re_term = 0
                        buy_prise = arr[i]
                    elif arr[i-1] not in sort_arr or arr[i-1] > arr[i]:
                        profit += re_term - buy_prise
                        re_term = 0
                        buy_prise = arr[i]
                    else:
                        if arr[i] > re_term:
                            re_term = arr[i]
                except:
                    pass
        else:
            if arr[i] > re_term and buy_prise != 0:
                re_term = arr[i]
            elif buy_prise == 0:
                if arr[i+1] > arr[i]:
                    buy_prise = arr[i]
    profit += re_term - buy_prise
    # print(profit, re_term, buy_prise)
    if profit > 0:
        print(profit)
    else:
        print(0)
