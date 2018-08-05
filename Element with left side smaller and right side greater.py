for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    flag = 0
    for i in range(1, n-1):
        k = arr[:i]
        m = arr[i+1:]
        if arr[i] > max(k) and arr[i] < min(m):
            flag = 1
            ans = arr[i]
            break
    if flag == 0:
        print(-1)
    else:
        print(ans)
