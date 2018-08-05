for _ in range(int(input())):
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = list(map(int, input().split()))

    if arr1[0] != 1:
        arr1[1] = arr1[1]/arr1[0]
        arr1[2] = arr1[2]/arr1[0]
        arr1[0] = arr1[0]/arr1[0]
    if arr2[0] != 0:
        k = arr2[0]
        for i in range(3):
            arr2[i] = int(arr2[i] - (k*arr1[i]))
    if arr3[0] != 0:
        k = arr3[0]
        for i in range(3):
            arr3[i] = int(arr3[i] - (k*arr1[i]))

    p = m = 1
    if arr3[1] != 0 and arr3[2] == 0:
        arr2[1] = arr2[1] / arr3[1]
    elif arr3[1] == 0 and arr3[2] != 0:
        arr2[2] = arr2[2] / arr3[2]
    elif arr3[1] != 0 and arr3[2] != 0:
        arr2[1] = arr2[1] / arr3[1]
        arr2[2] = arr2[2] / arr3[2]

    if arr2[1] == arr2[2]:
        arr2[1] = arr2[2] = 0

    if arr2.count(0) == 3 and arr3.count(0) != 3:
        print(2)
    elif arr3.count(0) == 3 and arr2.count(0) != 3:
        print(2)
    elif arr3.count(0) == 3 and arr2.count(0) == 3 and arr1.count(0) != 3:
        print(1)
    elif arr3.count(0) == 3 and arr2.count(0) == 3 and arr1.count(0) == 3:
        print(0)
    else:
        print(3)

    print(arr2)
    print(arr3)