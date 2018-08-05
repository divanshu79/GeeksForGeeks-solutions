for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    ones = []
    tows = []
    zeros = []
    for i in arr:
        if i == 0:
            zeros.append(i)
        elif i == 1:
            ones.append(1)
        else:
            tows.append(2)

    ans = []
    ans.extend(zeros)
    ans.extend(ones)
    ans.extend(tows)

    anss = ''
    for i in range(len(ans)):
        anss += str(ans[i]) + " "
    print(anss)
