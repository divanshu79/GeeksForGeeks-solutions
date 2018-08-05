def recursive_remove(n):
    previous_value = ''
    ans = ''
    guilty = ''
    for i in range(len(n)+1):
        if i == 0:
            previous_value = n[i]
        else:
            try:
                if previous_value == n[i]:
                    previous_value = n[i]
                    guilty = n[i]
                else:
                    if previous_value != guilty:
                        ans += previous_value
                        guilty = ''
                    previous_value = n[i]
            except:
                if previous_value != guilty:
                    ans += previous_value
    return ans


for _ in range(int(input())):
    n = input()
    while True:
        if len(n) > 0:
            m = recursive_remove(n)
            if len(n) != len(m):
                n = m
            else:
                break
        else:
            break
    print(n)