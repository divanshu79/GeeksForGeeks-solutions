for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = []
    check_sum = 0
    index = 0
    for i in arr:
        check_sum += i
        ans.append(i)
        index += 1
        if check_sum > x:
            while check_sum > x:
                p = ans.pop(0)
                check_sum -= p
                if check_sum == x:
                    print(index - len(ans) + 1, index)
                    break

        elif check_sum == x:
            print(index - len(ans) + 1, index)
            break
    print(check_sum)
