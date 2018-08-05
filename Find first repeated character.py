from collections import defaultdict

for _ in range(int(input())):
    n = input()
    def_dict = defaultdict(int)

    flag = ''
    for i in n:
        if def_dict[i] < 1:
            def_dict[i] += 1
        else:
            flag = i
            break

    if flag == '':
        print(-1)
    else:
        print(flag)