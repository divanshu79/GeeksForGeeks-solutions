for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    previous_number = -1
    ans = ''

    for i in range(n):
        if i == 0:
            previous_number = arr[i]
            ans += '1' + " "
        else:
            if previous_number > arr[i]:
                ans += '1' + " "
                previous_number = arr[i]
            else:
                num_list = arr[:i][::-1]
                previous_number = arr[i]
                p = 0
                for j in range(len(num_list)):
                    if num_list[j] <= arr[i]:
                        p += 1
                    else:
                        break
                ans += str(p+1) + " "
                # print('num_list')
                # print(num_list)
        # print('previous_number: ' + str(previous_number))
        # print('ans: ' + ans)
    print(ans)