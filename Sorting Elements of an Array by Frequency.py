from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    def_dict = defaultdict(int)
    a = []

    for i in arr:
        if def_dict[i] == 0:
            a.append(i)
        def_dict[i] += 1

    ch_list = []
    ch_dict = defaultdict(list)
    d_dict = defaultdict(int)
    for i in range(len(a)):
        k = def_dict[a[i]]
        if d_dict[k] == 0:
            ch_list.append(k)
            d_dict[k] += 1
        ch_dict[k].append(a[i])
    ans = ''
    ch_list.sort(reverse=True)
    for i in ch_list:
        lis = ch_dict[i]
        lis.sort()
        for j in range(len(lis)):
            k = i
            while k != 0:
                ans += str(lis[j]) + " "
                k -= 1
    print(ans)
