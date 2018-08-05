for _ in range(int(input())):
     n = int(input())
     arr = list(map(int,input().split()))
     arr.sort()

     listLen = len(arr)

     ans = ''
     for i in range(0,listLen,2):
          try:
               ans += str(arr[i+1] )+ " "+str(arr[i])+" "
          except:
               ans += str(arr[i]) + ' '

     print(ans)
