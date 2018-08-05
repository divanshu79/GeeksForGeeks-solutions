for _ in range(int(input())):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    check_arr = []
    index = 0
    sum = 0
    for i in range(n):
        if sum != s:
            sum += arr[i]
            check_arr.append(arr[i])
            index = i+1

        if sum > s:
            while sum > s:
                k = check_arr[0]
                check_arr.pop(0)
                sum -= k
                if sum == s:
                    break
        elif sum == s:
            break
    if sum == s:
        print(index-(len(check_arr)-1), index)
    else:
        print(-1)
