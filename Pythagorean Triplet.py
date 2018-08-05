from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    def_dict = defaultdict(int)
    sq_list = []
    for i in arr:
        def_dict[i*i] = 1
        sq_list.append(i*i)
    sum_list = []
    flag = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if def_dict[sq_list[i] + sq_list[j]] == 1:
                flag = 1
                print(arr[i], arr[j])
                break
        if flag == 1:
            break

    if flag == 1:
        print('Yes')
    else:
        print('No')