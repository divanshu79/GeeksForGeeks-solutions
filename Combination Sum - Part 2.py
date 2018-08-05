from itertools import combinations
from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    tot_sum = int(input())
    arr.sort()
    ans = ''
    ans_list = []
    def_dict = defaultdict(int)
    for i in range(n-1, -1, -1):
        all_combinations = combinations(arr, i)
        for j in all_combinations:
            if def_dict[str(j)] == 0:
                if sum(j) == tot_sum:
                    ans_list.append(j)
                def_dict[str(j)] += 1
    dd_dict = defaultdict(int)
    ap = []
    for i in ans_list:
        if dd_dict[i[0]] == 0:
            ap.append(i[0])
        dd_dict[i[0]] += 1

    while len(ap) > 0:
        r = 0
        for i in ans_list:
            if dd_dict[ap[0]] > 0:
                if i[0] == ap[0]:
                    ans += '('
                    for k in i:
                        ans += str(k) + " "
                    ans = ans[:len(ans)-1]
                    ans += ')'
                    dd_dict[ap[0]] -= 1
                    ans_list.pop(r)
                    if dd_dict[ap[0]] == 0:
                        ap.pop(0)
                r += 1

    if len(ans) > 0:
        print(ans)
    else:
        print('Empty')