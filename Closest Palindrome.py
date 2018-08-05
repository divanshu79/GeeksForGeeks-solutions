for _ in range(int(input())):
    n = input()
    pre = n[0]
    post = n[len(n)-1]
    mi = n[1:len(n)-1]
    if pre == post == '1' and mi.count('0') == len(mi) and len(n) > 1:
        print(str(int(n)-2))
    else:
        if n != n[::-1]:
            mid = len(n)//2-1
            if n[mid] != '0':
                pass
            elif n[mid] == '0' and n[mid+1] != '0':
                k = list(n)
                k[mid] = k[mid+1] = '1'
                kk = ''
                for i in range(len(k)):
                    kk += k[i]
                n = kk

            for i in range(len(n) // 2):
                try:
                    n = n[:len(n) - 1 - i] + n[i] + n[len(n) - i:]
                except:
                    n = n[:len(n) - 1 - i] + n[i]


            print(n)
        else:
            if len(n) != 1:
                if n.count('9') != len(n):
                    mid = len(n)//2
                    if len(n)%2 != 0:
                        if n[mid] != '0':
                            n = n[:mid]+str(int(n[mid])-1)+n[mid+1:]
                        else:
                            if n[mid-1] != '0':
                                n = n[:mid]+str(int(n[mid])+1)+n[mid+1:]
                            else:
                                k = list(n)
                                k[mid] = '9'
                                for i in range(mid-1,-1,-1):
                                    if n[i] != '0':
                                        k[i] = str(int(n[i])-1)
                                        k[len(n)-1-i] = str(int(n[i])-1)
                                        break
                                    else:
                                        k[i] = '9'
                                        k[len(n)-1-i] = '9'
                                kk = ''
                                for i in range(len(k)):
                                    kk += k[i]
                                # print(k)
                                n = kk

                    else:
                        if n[mid] != '0':
                            n = n[:mid-1]+str(int(n[mid-1:mid])-1)+str(int(n[mid:mid+1])-1)+n[mid+1:]
                        elif n[mid] == '0' and len(n) > 2:
                            k = list(n)
                            if n[mid+1] != "0":
                                n = n[:mid-2]+str(int(n[mid-2:mid+2])-11)+n[mid+2:]
                            else:
                                mid = mid-1
                                k[mid] = k[mid+1] = '9'
                                for i in range(mid-1,-1,-1):
                                    if n[i] != '0':
                                        k[i] = str(int(n[i]) - 1)
                                        k[len(n) - 1 - i] = str(int(n[i]) - 1)
                                        break
                                    else:
                                        k[i] = '9'
                                        k[len(n) - 1 - i] = '9'
                                kk = ''
                                for i in range(len(k)):
                                    kk += k[i]
                                # print(k)
                                n = kk
                        elif n == '00':
                            n = '11'

                else:
                    n = str(int(n)+2)
                print(n)

            else:
                if n != '0':
                    print(str(int(n)-1))
                else:
                    print('1')
