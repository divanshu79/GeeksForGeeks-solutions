from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    com_n = n*2+2
    arr = list(map(int, input().split()))

    est_dict = defaultdict(list)
    check_dict = defaultdict(int)

    for i in range(com_n):
        if check_dict[arr[i]] == 0:
            est_dict[1].append(arr[i])
            check_dict[arr[i]] += 1
            check_dict[arr[i]] = check_dict[arr[i]] % 2
        elif check_dict[arr[i]] == 1:
            k = est_dict[1].index(arr[i])
            est_dict[2].append(arr[i])
            est_dict[1].pop(k)
            check_dict[arr[i]] += 1
            check_dict[arr[i]] = check_dict[arr[i]] % 2
    if len(est_dict[1]) == 2:
        if est_dict[1][0] > est_dict[1][1]:
            print(est_dict[1][1], est_dict[1][0])
        else:
            print(est_dict[1][0], est_dict[1][1])
    else:
        print(0, 0)
