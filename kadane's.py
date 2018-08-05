t=int(input())
for _ in range(t):
    n=int(input())
    v=list(map(int,input().split()))
    ma=-101
    c=0
    for i in range(n):
       c=c+v[i]
       c=max(c,v[i])
       ma=max(ma,c)
    print(ma)