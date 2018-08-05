from collections import defaultdict
for _ in range(int(input())):
    x = int(input())
    arr_dict = list(map(str, input().split()))
    arr_dict = sorted(set(arr_dict))
    n, m = map(int, input().split())
    arr_char = list(map(str, input().split()))

    char_dict = defaultdict(int)
    def_dict = defaultdict(list)

    for i in arr_char:
        char_dict[i] += 1
        for j in arr_dict:
            if i in j and j.count(i) >= char_dict[i]:
                def_dict[j].append(i)
    ans = ''
    print(def_dict)
    for i in arr_dict:
        if len(i) == len(def_dict[i]):
            ans += i + " "
    if len(ans) > 0:
        print(ans)
    else:
        print(-1)
