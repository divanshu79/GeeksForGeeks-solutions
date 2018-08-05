from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    def_dict = defaultdict(int)
    for i in arr:
        def_dict[i] += 1

    all_sum = []
    for i in range(n-1):
        for j in range(i+1, n):
            k = arr[i] + arr[j]
            all_sum.append((k, arr[i], arr[j]))

    flag = 0
    for i in range(len(all_sum)):
        k = all_sum[i]
        k_neg = -1*k[0]
        m = def_dict[k[1]] - 1
        p = def_dict[k[2]] - 1
        ans = def_dict[k_neg] -1
        if k_neg != k[1] and k_neg != k[2]:
            if def_dict[k_neg] > 0 and m >= 0 and p >= 0:
                flag = 1
                break
        else:
            if def_dict[k_neg] > 1 and m >= 0 and p >= 0:
                flag = 1
                break

    if flag == 1:
        print(1)
    else:
        print(0)
