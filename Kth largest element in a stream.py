for _ in range(int(input())):
    k, n = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr)
    p = k-1
    ans = ''
    j = 0
    for i in range(n):
        if p == 0:
            ans += str(arr[j]) + " "
            j += 1
        else:
            ans += '-1' + " "
            p -= 1
    # print(ans)
