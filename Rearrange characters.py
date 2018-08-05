from collections import defaultdict
for _ in range(int(input())):
    n = input()
    def_dict = defaultdict(int)
    k = []
    for i in n:
        if def_dict[i] == 0:
            k.append(i)
        def_dict[i] += 1
    arr = []
    for i in k:
        m = def_dict[i]
        arr.append((m, i))
    arr.sort(reverse=True)

    high = arr[0][0]
    max_other = 0
    flag = 0
    for i in range(1,len(arr)):
        max_other += arr[i][0]
        if max_other + 1 >= high:
            flag = 1
            break
    if flag == 0:
        print(0)
    else:
        print(1)