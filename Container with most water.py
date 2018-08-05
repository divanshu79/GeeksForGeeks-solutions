for _ in range(int(input())):
    n = int(input())
    num = list(map(int, input().split()))

    res = []

    for i in range(n-1):
        for j in range(i+1, n):
            res.append((j-i)*min(num[i], num[j]))
    print(max(res))