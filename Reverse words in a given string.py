for _ in range(int(input())):
    n = input()
    ans = ''
    sub_ans = ''
    for i in range(len(n)):
        if n[i] != '.':
            sub_ans += n[i]
        else:
            ans = sub_ans+ "." + ans
            sub_ans = ''
    if len(sub_ans) != 0:
        if n.count('.') > 0:
            print(sub_ans + '.' + ans[:len(ans)-1])
        else:
            print(sub_ans)
    else:
        print(ans[:len(ans)-1])