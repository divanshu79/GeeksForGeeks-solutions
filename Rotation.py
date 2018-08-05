for _ in range(int(input())):
     n = int(input())
     arr = list(map(int,input().split()))

     minVal = min(arr)
     maxVal = max(arr)
     indVal1 = arr.index(minVal)
     indVal2 = arr.index(maxVal)
     count_max = arr.count(maxVal)
     count_min = arr.count(minVal)

     listlen = len(arr)
     maxind = listlen - 1

     if indVal1 == 0 and arr[maxind] == maxVal:
          print('sdbjan')
          print(0)
     elif indVal1 == 0 and arr[maxind] == minVal:
          print(indVal2+count_max)
     else:
          print(indVal1)
