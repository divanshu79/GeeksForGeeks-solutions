for _ in range(int(input())):
    n = int(input())
    pl_array = list(map(int, input().split()))

    i = 0
    c = 0
    while 1:
        if i != (len(pl_array)//2):
            if pl_array[i] != pl_array[len(pl_array)-i-1]:
                if pl_array[i] > pl_array[len(pl_array)-i-1]:
                    ex_arr = [pl_array[len(pl_array)-i-1], pl_array[i] - pl_array[len(pl_array)-i-1]]
                    pl_array = pl_array[:i]+ex_arr[:]+pl_array[i+1:]
                else:
                    ex_arr = [pl_array[len(pl_array) - i-1] - pl_array[i], pl_array[i]]
                    pl_array = pl_array[:len(pl_array)-i-1]+ex_arr[:]+pl_array[len(pl_array)-i:]
                c += 1
                # print(pl_array)
            i += 1
        else:
            break
    print(c)