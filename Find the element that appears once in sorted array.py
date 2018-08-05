from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    def_dict = defaultdict(int)
    for i in arr:
        def_dict[i] += 1
    for i in arr:
        if def_dict[i] == 1:
            print(i)
            break
