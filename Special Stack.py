def push(arr, ele):
    return arr.append(ele)


def pop(arr):
    return arr.pop(0)


def isFull(n, arr):
    if n == len(arr):
        return 1
    else:
        return 0


def isEmpty(arr):
    if len(arr) > 0:
        return 1
    else:
        return 0


def getMin(n, arr):
    i = 0
    while isEmpty(arr) == 1:
        if i == 0:
            k = pop(arr)
            n = k
        else:
            k = pop(arr)
            if k < n:
                n = k
        i += 1
    return n


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        stack = []
        ans = 10000000
        for i in range(n):
            push(stack, arr[i])
        print(getMin(n, stack))
