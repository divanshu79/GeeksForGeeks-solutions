def rotate(a,k):
     list = a[k:]+a[:k]
     return list

for _ in range(int(input())):
     n,k = list(map(int,input().split()))
     a = list(map(int,input().split()))
     k = k%n
     a = rotate(a,k)
     l = ''

     for i in range(len(a)):
          l += str(a[i])+' '
     print(l[:len(l)-1])
