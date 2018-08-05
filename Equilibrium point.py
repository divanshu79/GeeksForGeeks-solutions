for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    index = -1
    if n == 1:
        print(1)
    else:
        for i in range(n):
            m = arr[:i]
            p = arr[i+1:]
            if sum(m) == sum(p):
                index = i+1
                break
        if index == -1:
            print(-1)
        else:
            print(index)
