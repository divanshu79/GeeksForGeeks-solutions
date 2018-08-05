for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())

    arr.sort()
    print(arr[k-1])