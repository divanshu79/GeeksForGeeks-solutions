for _ in range(int(input())):
    n = int(input())
    arr = [0]*(n+1)
    if n >= 7:
        for i in range(7):
            arr[i] = i
        for i in range(7, n+1):
            arr[i] = arr[i-1] + 1

            for j in range(i-3, 0, -1):
                arr[i] = max(arr[i], arr[j]*(i-j-1))
        print(arr[n])
    elif n < 7:
        print(n)
    elif n > 75:
        print(-1)