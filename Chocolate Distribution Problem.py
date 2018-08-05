for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    no_stud = int(input())
    arr.sort()

    minimum = 10000000
    for i in range(n-no_stud+1):
        k = arr[i:i+no_stud]
        mn = k[no_stud-1] - k[0]
        if mn < minimum:
            minimum = mn
    print(minimum)
