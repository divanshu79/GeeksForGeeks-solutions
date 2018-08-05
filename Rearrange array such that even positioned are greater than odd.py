for _ in range(int(input())):
     n = int(input())
     arr = list(map(int,input().split()))
     arr.sort()

     ans = ''
     for i in range(0,n//2):
          try:
               ans += str(arr[i]) + ' '+ str(arr[n-i-1]) +' '
          except:
               ans += str(arr[i])+ ' '
     if n%2 == 0:
          print(ans)
     else:
          print(ans+str(arr[n//2]))
