for _ in range(int(input())):
    number = int(input())
    number_len = len(str(number))
    s = []
    while number > 0:
        k = ''
        ast = str(number)
        for i in range(len(ast)):
            if ast[i] != '0':
                k += '1'
            else:
                k += '0'
        s.append(k)
        number -= int(k)

    ans = ''
    for i in range(len(s)):
        ans += s[i]+' '

    print(ans)
