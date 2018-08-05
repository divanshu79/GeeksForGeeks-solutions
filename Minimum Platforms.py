from operator import itemgetter
for _ in range(int(input())):
     n = int(input())
     arrival = list(map(int,input().split()))
     departire = list(map(int,input().split()))

     arr = []
     for i in range(n):
          arrival[i] = arrival[i]/100
          departire[i] =departire[i]/100
          arr.append((arrival[i],0))
          if arrival[i] > departire[i]:
               k = arrival[i] + (24-arrival[i]) + departire[i]
          else:
               k = departire[i]
          arr.append((k,1))
     arr.sort(key=itemgetter(0))
     c = 0
     p = 0

     for i in range(len(arr)):
          if arr[i][1] == 0:
               if p == c:
                    p = p + 1
                    c += 1
               elif p > c:
                    c += 1
          elif arr[i][1] == 1:
               c -= 1
     print(p)
