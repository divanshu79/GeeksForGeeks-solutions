from operator import itemgetter

for _ in range(int(input())):
     n,k = map(int,input().split())
     arr = list(map(int,input().split()))

     sArr = []
     for i in range(n):
          sArr.append((abs(arr[i]-k),arr[i]))

     sArr.sort(key=itemgetter(0))
     ans = ''
     for i in range(n):
          ans += str(sArr[i][1])+' '
     print(ans)
