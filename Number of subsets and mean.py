for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    min = arr.count(arr[0])
    max = arr.count(arr[n-1])
    min = pow(2, min) % (pow(10, 9) + 7)
    max = pow(2, max) % (pow(10, 9) + 7)

    print(max-1, min-1)
