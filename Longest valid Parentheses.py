from collections import defaultdict
for _ in range(int(input())):
    n = input()
    len_input = len(n)

    ans = 0
    flag = 0
    ans_dict = defaultdict(list)
    sec_dict = defaultdict(int)
    k = 0
    for i in range(len_input):
        if n[i] == '(':
            if flag == 0:
                ans_dict[k].append(n[i])
            else:
                k += 1
                ans_dict[k].append(n[i])
                flag = 0
        elif n[i] == ')':
            try:
                if len(ans_dict[k]) == 0:
                    k -= 1
                    flag = 1
                    sec_dict[k] = sec_dict[k] + sec_dict[k+1]
                    sec_dict[k + 1] = 0
                    ans_dict[k].pop(0)
                    sec_dict[k] += 1
                    if ans < sec_dict[k]:
                        ans = sec_dict[k]
                    if len(ans_dict[k]) == 0:
                        k -= 1
                        sec_dict[k] = sec_dict[k] + sec_dict[k+1]
                        sec_dict[k + 1] = 0
                        if ans < sec_dict[k]:
                            ans = sec_dict[k]
                else:
                    ans_dict[k].pop(0)
                    sec_dict[k] += 2
                    flag = 1
                    if ans < sec_dict[k]:
                        ans = sec_dict[k]
                    if len(ans_dict[k]) == 0:
                        k -= 1
                        sec_dict[k] = sec_dict[k] + sec_dict[k+1]
                        sec_dict[k+1] = 0
                        if ans < sec_dict[k]:
                            ans = sec_dict[k]
            except:
                sec_dict.clear()
                ans_dict.clear()

    print(ans)
