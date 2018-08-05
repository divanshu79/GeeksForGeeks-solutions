for _ in range(int(input())):
     n = int(input())
     s = []
     x = 0
     for i in range(n):
          p = ''
          for j in range(n):
               if i == 0 or i == n-1:
                    p += chr(65+x)
                    x += 1
               else:
                    if j == 0 or j == n-1:
                         p += chr(65+x)
                         x += 1
                    else:
                         p += '$'
          s.append(p)

     for i in s:
          print(i)
