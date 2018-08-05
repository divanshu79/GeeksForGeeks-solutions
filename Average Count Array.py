from collections import defaultdict
for _ in range(int(input())):
    a, x = map(int, input().split())
    list_a = list(map(int, input().split()))
    dict = defaultdict(int)
    result = ''

    for i in list_a:
        dict[i] += 1

    for i in range(a):
        mean = (list_a[i]+x)//2
        result += str(dict[mean])+" "
    print(result)
