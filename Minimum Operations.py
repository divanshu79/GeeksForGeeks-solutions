def opp(k, c):
    if k == 2:
        return c+2
    else:
        if k % 2 == 0:
            c += 1
            return opp(k//2, c)
        else:
            c += 1
            k -= 1
            return opp(k, c)


for _ in range(int(input())):
    n = int(input())
    count = 0
    if n != 1 and n!= 0:
        if n % 2 == 0:
            count += opp(n, count)
        else:
            count += opp(n, count)
    else:
        if n == 1:
            print(1)
        else:
            print(0)
    print(count)
