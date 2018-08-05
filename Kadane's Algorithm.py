for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ini_sum = 0
    pre_check = ''
    if max(arr) < 0:
        print(max(arr))
    else:
        sums = []
        for i in arr:
            if pre_check == '':
                if i >= 0:
                    pre_check = 'p'
                    ini_sum += i
                else:
                    pre_check = 'n'
                    ini_sum += i
            elif pre_check == 'p':
                if i >= 0:
                    ini_sum += i
                else:
                    pre_check = 'n'
                    sums.append(ini_sum)
                    ini_sum = i
            elif pre_check == 'n':
                if i >= 0:
                    pre_check = 'p'
                    sums.append(ini_sum)
                    ini_sum = i
                else:
                    ini_sum += i
        sums.append(ini_sum)

        ans = []
        for i in range(len(sums)-1):
            k = sums[i]
            ans.append(k)
            for j in range(i+1, len(sums)):
                k += sums[j]
                ans.append(k)
        ans.append(sums[len(sums)-1])
        print(max(ans))
