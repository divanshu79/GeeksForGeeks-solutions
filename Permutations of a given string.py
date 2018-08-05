import itertools
for _ in range(int(input())):
    n = input()
    n = sorted(n)

    ans = ''
    for p in itertools.permutations(n):
        k = p
        for i in range(len(k)):
            ans += k[i]
        ans += " "
    print(ans)