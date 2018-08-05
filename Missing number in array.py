from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    def_dict = defaultdict(int)
    for i in arr:
        def_dict[i] = 1
    ans = 0
    for i in range(1,n+1):
        if def_dict[i] == 0:
            ans = i
            break
    if ans == 0:
        print(n)
    else:
        print(ans)
