n = int(input())
k = int(input())

arr = 0
for i in range(1, n+1):
    m = (pow(i, k) - pow(i-1, k))
    arr += m
print(arr % (pow(10, 9) + 7))