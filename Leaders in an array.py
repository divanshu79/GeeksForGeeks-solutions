for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = ''
    for i in range(n-1):
        m = arr[i+1:]
        if arr[i] > max(m):
            ans += str(arr[i]) + " "
    if n > 1:
        print(ans+str(arr[n-1]))
    else:
        print(arr[n-1])
