for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    buy_day = -1000000
    check_price = 0
    profit = ''
    for i in range(len(arr)):
        if buy_day == -1000000:
            buy_day = i
            check_price = arr[i]
        else:
            if arr[i] >= check_price:
                check_price = arr[i]
            else:
                if buy_day == i-1:
                    buy_day = i
                    check_price = arr[i]
                else:
                    profit += "(" + str(buy_day) + " " + str(i-1) + ")" + " "
                    buy_day = i
                    check_price = arr[i]

    if check_price - arr[buy_day] > 0:
        print(profit + "(" + str(buy_day) + " " + str(len(arr)-1) + ")")
    else:
        if len(profit) == 0:
            print("No Profit")
        else:
            print(profit)
