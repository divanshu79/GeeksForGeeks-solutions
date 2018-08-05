from collections import defaultdict
for _ in range(int(input())):
    n = input()
    m = input()
    def_dict = defaultdict(int)

    for i in n:
        def_dict[i] += 1
    flag = 0
    if len(m) == len(n):
        for i in m:
            if def_dict[i] > 0:
                def_dict[i] -= 1
            else:
                flag = 1
                break
        if flag == 0:
            print("YES" )
        else:
            print("NO")
    else:
        print("NO")