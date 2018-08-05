for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = ''

    for i in range(n):
        try:
            k = arr[i+1:]
            p = -1
            for j in k:
                if j > arr[i]:
                    p = j
                    break
            ans += str(p) + " "
        except:
            ans += '-1'
    print(ans)