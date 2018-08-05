from collections import defaultdict
for _ in range(int(input())):
    m, n = map(int, input().split())
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))

    def_dict = defaultdict(int)
    for i in arr_1:
        def_dict[i] = 1

    flag = 0
    for i in arr_2:
        if def_dict[i] == 0:
            flag = 1
    if flag == 0:
        print("Yes")
    else:
        print('No')