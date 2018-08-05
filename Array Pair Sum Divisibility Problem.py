for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())

    flag = 0
    if n % 2 == 0:
        i = 0
        j = 1
        while len(arr) > 0:
            if j <= len(arr) - 1:
                if (arr[i] + arr[j]) % k == 0:
                    arr.pop(i)
                    arr.pop(j-1)
                    j = 1
                else:
                    j += 1
            else:
                flag = 1
                break
    else:
        flag = 1

    if flag == 0:
        print('True')
    else:
        print('False')