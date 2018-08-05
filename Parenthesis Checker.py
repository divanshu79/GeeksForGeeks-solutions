for _ in range(int(input())):
    n = input()
    p = n
    ans = []
    flag = 0
    for i in range(len(n)):
        if n[i] == "{" or n[i] == "[" or n[i] == "(":
            ans.append(n[i])
        else:
            if len(ans) > 0:
                if (n[i] == '}' and ans[len(ans)-1] == '{') or \
                        (n[i] == ']' and ans[len(ans)-1] == '[') or \
                        (n[i] == ')' and ans[len(ans)-1] == '('):
                    ans.pop(len(ans)-1)
                    flag = 0
                else:
                    flag = 1
                    break
            else:
                flag = 1
                break
        # print(ans)
    if flag == 1:
        print('not balanced')
    else:
        if len(ans) == 0:
            print('balanced')
        else:
            print('not balanced')