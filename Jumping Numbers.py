for _ in range(int(input())):
    n = int(input())
    len_n = len(str(n))
    ans = '0 '
    number = []

    for i in range(1, 10):
        ans += str(i) + " "
        number.append(i)
        while len(number) != 0:
            # if len(str(number[0])) < len_n:
            lst_num = number[0] % 10
            if lst_num != 0 and lst_num != 9:
                k = lst_num - 1
                m = lst_num + 1
                small = str(number[0]) + str(k)
                large = str(number[0]) + str(m)
                if int(small) <= n:
                    ans += small + " "
                    number.append(int(small))
                if int(large) <= n:
                    ans += large + " "
                    number.append((int(large)))
                number.pop(0)
            elif lst_num == 9:
                k = lst_num - 1
                small = str(number[0]) + str(k)
                if int(small) <= n:
                    ans += small + " "
                    number.append(int(small))
                number.pop(0)
            elif lst_num == 0:
                m = lst_num + 1
                large = str(number[0]) + str(m)
                if int(large) <= n:
                    ans += large + " "
                    number.append((int(large)))
                number.pop(0)
            # else:
            #     # ans += str(number[0]) + " "
            #     number.pop(0)
    print(ans)

