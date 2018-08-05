for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = []
    for i in range(1,n+1):
        arr.append(i)

    for i in range(n-1):
        p = k
        if len(arr) < k:
            p = k % len(arr)
            if p == 0:
                p = len(arr)
        arr = arr[p:] + arr[:p-1]
    print(arr[0])