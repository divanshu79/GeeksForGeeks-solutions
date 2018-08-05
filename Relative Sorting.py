from collections import defaultdict

for _ in range(int(input())):
    m, n = map(int, input().split())
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))

    def_dict = defaultdict(int)
    check_dict = defaultdict(int)
    for i in arr_1:
        def_dict[i] += 1

    ans = ''
    for i in arr_2:
        k = def_dict[i]
        check_dict[i] = 1
        while k != 0:
            ans += str(i) + " "
            k -= 1
    arr_1.sort()
    for i in arr_1:
        if check_dict[i] != 1:
            ans += str(i) + " "
    print(ans)
