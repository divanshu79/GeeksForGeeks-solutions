def GetMinStr(n, i, j):
    if i < j:
        if n[i] == n[j]:
            return GetMinStr(n, i+1, j-1)
        else:
            return 1 + min(GetMinStr(n, i+1, j), GetMinStr(n, i, j-1))
    else:
        return 0


for _ in range(int(input())):
    n = input()
    p = len(n)
    if p == 1:
        print(0)
    else:
        l = 0
        h = p-1
        a = GetMinStr(n, l, h)
        print(a)