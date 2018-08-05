from operator import itemgetter
from collections import defaultdict
for _ in range(int(input())):
     n,x,y = map(int,input().split())
     a = list(map(int,input().split()))
     b = list(map(int,input().split()))

     arr = []
     for i in range(n):
          arr.append((a[i],i,0))
          arr.append((b[i],i,1))
     arr.sort(key=itemgetter(0), reverse = True)

     val = [0]*n
     for i in range(len(arr)):
          t = arr[i][1]
          valInd = arr[i][0]
          d = arr[i][2]
          if val[t] == 0:
               if d == 0 and x > 0:
                    val[t] = valInd
                    x  -= 1
               elif d == 1 and y > 0:
                    val[t] = valInd
                    y -= 1
     print(sum(val))
                    
