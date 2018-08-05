from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    def_dict = defaultdict(int)

    for i in range(len(arr_b)):
        if def_dict[arr_b[i]] < arr_a[i]:
            def_dict[arr_b[i]] = arr_a[i]

    sort_b = sorted(arr_b)
    tot_selection = 0
    check = []
    min_no = 0
    for i in range(len(arr_b)):
        k = sort_b[i]
        if def_dict[k] >= min_no:
            min_no = k
            check.append(k)
            tot_selection += 1
    print(tot_selection + n - len(arr_b))
