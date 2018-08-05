for _ in range(int(input())):
    n = input()
    length = len(n)
    low = high = 0
    start = 0
    max_length = 1

    for i in range(1, length):
        # even length string
        low = i-1
        high = i
        while low >= 0 and high < length and n[low] == n[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1

        # odd length string
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and n[low] == n[high]:
            if high - low + 1 > max_length:
                start = low
                max_length = high - low + 1
            low -= 1
            high += 1
    print(n[start:start + max_length])