for _ in range(int(input())):
     a = input()
     c = 0
     for i in range(len(a)):
          if a[i] == '2':
               if a[i+1] == '1':
                    c+= 1
     print(c)
