from collections import defaultdict

for _ in range(int(input())):
    n, m, x = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_a.sort()
    arr_b = list(map(int, input().split()))

    def_dict = defaultdict(int)
    for i in range(len(arr_b)):
        def_dict[arr_b[i]] = 1

    ans = ''
    for i in range(len(arr_a)):
        if def_dict[x-(arr_a[i])] == 1:
            ans += str(arr_a[i]) + " " + str(x - arr_a[i]) + ","
    if len(ans) > 0:
        print(ans[:len(ans)-1])
    else:
        print(-1)
