from collections import defaultdict

def_dict = defaultdict(int)
fib_dict = defaultdict(int)

for i in range(1000):
    if i == 0:
        def_dict[i] = 0
    elif i == 1:
        def_dict[i] = 1
    else:
        def_dict[i] = def_dict[i-1] + def_dict[i-2]
    fib_dict[def_dict[i]] = 1

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = ''

    for i in arr:
        if fib_dict[i] == 1:
            ans += str(i) + " "
    print(ans)
