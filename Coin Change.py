from collections import defaultdict
for _ in range(int(input())):
    m = int(input())
    arr = list(map(int, input().split()))
    arr = list(set(arr))
    n = int(input())
    def_dict = defaultdict(list)
    count = 0
    for i in range(m):
        total = 0
        while total < n:
            total += arr[i]
            if len(def_dict[n-total]) != 0:
                k = def_dict[total]
                for x in k:
                    count += len(def_dict[x])
            def_dict[total].append(arr[i])
        if total == n:
            count += 1
        print('count: ' + str(count))
        print('total: ' + str(total))
    print(count)
    print(def_dict)