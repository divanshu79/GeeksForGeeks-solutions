for _ in range(int(input())):
     n,s = list(map(int,input().split()))
     l = list(map(int,input().split()))

     try:
          ind = l.index(s)
          print(ind)
     except:
          print("OOPS! NOT FOUND")
