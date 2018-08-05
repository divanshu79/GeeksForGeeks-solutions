for _ in range(int(input())):
    n = int(input())
    mice = list(map(int, input().split()))
    hole = list(map(int, input().split()))

    mice.sort()
    hole.sort()
    result = []

    for i in range(n):
        result.append(abs(mice[i]-hole[i]))
    print(max(result))