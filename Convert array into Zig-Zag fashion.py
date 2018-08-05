for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = ''
    for i in range(n-1):
        if i % 2 == 0:
            if arr[i] > arr[i+1]:
                t = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = t
        else:
            if arr[i] < arr[i+1]:
                p = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = p
        ans += str(arr[i]) + " "
    print(ans + str(arr[n-1]))