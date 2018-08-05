for _ in range(int(input())):
     n = int(input())
     arr1 = list(map(int,input().split()))
     p = len(arr1)
     i = 0

     res = []
     
     while(p != 0):
          try:
               if arr1[i] == arr1[i+1] and arr1[i] != 0:
                    res.append(2*arr1[i])
                    i += 2
                    p -= 2
               elif arr1[i] != arr1[i+1] and arr1[i] != 0:
                    res.append(arr1[i])
                    i += 1
                    p -= 1
               else:
                    i += 1
                    p -= 1
          except:
               if arr1[i] != 0:
                    res.append(arr1[i])
                    i += 1
                    p -= 1
               else:
                    i += 1
                    p -= 1

     ans = ''
     for i in range(n):
          try:
               ans += str(res[i]) + ' '
          except:
               ans += '0 '
     print(ans)
