{
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input().strip())
        if n:
            arr = list(map(int, input().strip().split()))
            print(max_sum(arr, n))
        else:
            print(0)
}

def max_sum(l,n):
     sum = 0
     s = 0
     for i in range(n):
          sum += l[i]
          s += i*l[i]

     max = s
     for i in range(1,n):
          s = s+sum-n*l[n-i]
          if s>max:
               max = s
     return max
