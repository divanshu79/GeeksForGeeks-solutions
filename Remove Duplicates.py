from collections import defaultdict
for _ in range(int(input())):
    n = input()
    def_dict = defaultdict(int)
    ans = ''

    for i in n:
        if def_dict[i] == 0:
            ans += i
            def_dict[i] += 1
    print(ans)