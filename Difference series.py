from collections import defaultdict
dfdict = defaultdict(int)
for i in range(1,101):
    if i == 1:
        dfdict[i] = 3
    else:
        dfdict[i] = dfdict[i-1] + 7 + 4*(i-2)
for _ in range(int(input())):
    n = int(input())
    print(dfdict[n])
