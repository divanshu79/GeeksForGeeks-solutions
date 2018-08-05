for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = [1]*n
    i = 0
    j = 1
    max_ans = 1
    if len(arr) > 0:
        while True:
            try:
                if arr[i] < arr[j]:
                    k = ans[i] + 1
                    if k > ans[j]:
                        ans[j] = k
                    if ans[j] > max_ans:
                        max_ans = ans[j]
                i += 1
                if i == j:
                    i = 0
                    j += 1
            except:
                break
        print(max_ans)
    else:
        print(0)