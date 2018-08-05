def iss(string, n):
    ans_str = []
    n = int(n)
    string_1 = string[:len(string)//2]
    i = 0
    j = 0
    flag = 0
    while len(string_1) != 0:
        if string[i] == string[len(string)-j-1]:
            ans_str.append(string[i])
            string_1 = string_1[1:]
            i += 1
            j += 1
        else:
            if len(string_1) - 1 == i:
                string_1 = string_1[1:]
                n -= 1
            elif len(string_1) - 1 != i:
                if string[i+1] == string[len(string)-j-1]:
                    if n >= 1:
                        string_1 = string_1[1:]
                        n -= 1
                        i += 1
                    else:
                        flag = 1
                        break
                elif string[i] == string[len(string)-j-2]:
                    if n >= 1:
                        string_1 = string_1[1:]
                        n -= 1
                        j += 2
                        i += 1
                    else:
                        flag = 1
                        break
                else:
                    if n >= 2:
                        string_1 = string_1[1:]
                        n -= 2
                        i += 1
                        j += 1
                    else:
                        flag = 1
                        break
    if flag == 0:
        return 1
    else:
        return 0


for _ in range(int(input())):
    string, n = map(str, input().split())
    print(iss(string, n))
