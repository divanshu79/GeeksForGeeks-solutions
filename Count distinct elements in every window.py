for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = ''
    for i in range(n-k+1):
        p = arr[i:i+k]
        ans += str(len(set(p))) + " "
    print(ans)