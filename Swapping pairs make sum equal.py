from collections import defaultdict
for _ in range(int(input())):
    m, n = map(int, input().split())
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))
    def_dict = defaultdict(int)

    for i in range(m):
        def_dict[arr_1[i]] = 1

    s = (sum(arr_1) - sum(arr_2))

    if s % 2 == 0:
         s = s//2
    flag = 0
    for i in range(n):
        if def_dict[s+arr_2[i]] == 1:
            flag = 1
            break
    if flag == 1:
        print(1)
    else:
        print(-1)