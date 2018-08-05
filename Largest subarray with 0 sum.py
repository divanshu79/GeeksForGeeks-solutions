from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    def_dict = defaultdict(int)

    arr_sum = 0
    ans = 0
    for i in range(n):
        arr_sum += arr[i]
        if def_dict[arr_sum] != 0:
            k = i - def_dict[arr_sum] + 1
            if k > ans:
                ans = k
        elif arr_sum == 0:
            k = i + 1
            if k > ans:
                ans = k
        else:
            def_dict[arr_sum] = i + 1
    print(ans)