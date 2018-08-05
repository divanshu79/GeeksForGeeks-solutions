from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict
arr = []
def_dict = defaultdict(int)
for _ in range(int(input())):
    n = int(input())
    if len(arr) == 0:
        arr.append(n)
        def_dict[n] = 1
        print(n)
    else:
        if len(arr) % 2 != 0:
            if def_dict[n] == 0:
                k = bisect_left(arr, n)
                def_dict[n] = 1
                arr = arr[:k] + [n] + arr[k:]
            else:
                m = bisect_right(arr, n)
                arr = arr[:m] + [n] + arr[m:]
            ans = (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) // 2
            print(ans)
        else:
            if def_dict[n] == 0:
                k = bisect_left(arr, n)
                def_dict[n] = 1
                arr = arr[:k] + [n] + arr[k:]
            else:
                m = bisect_right(arr, n)
                arr = arr[:m] + [n] + arr[m:]
            ans = arr[len(arr)//2]
            print(ans)