for _ in range(int(input())):
     n = int(input())
     arr = list(map(int,input().split()))

     pos = []
     neg = []

     lenLest = len(arr)

     for i in arr:
          if i >=0:
               pos.append(i)
          else:
               neg.append(i)

     maxVal = max(len(pos),len(neg))

     ans = ''
     for i in range(maxVal):
          if maxVal == len(pos):
               try:
                    ans += str(pos[i]) + " "+ str(neg[i])+" "
               except:
                    ans += str(pos[i])+" "
          else:
               try:
                    ans += str(pos[i]) + " "+ str(neg[i])+" "
               except:
                    ans += str(neg[i])+" "
     print(ans)
                    
