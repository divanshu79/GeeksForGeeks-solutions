for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    max_ind = 0
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if arr[i] <= arr[j]:
                k = j-i
                if max_ind < k:
                    max_ind = k
                break
    print(max_ind)
