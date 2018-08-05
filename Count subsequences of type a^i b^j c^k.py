for _ in range(int(input())):
    n = input()

    count_a = 0
    count_b = 0
    count_c = 0
    for i in range(len(n)):
        if n[i] == 'a':
            count_a = 1 + 2*count_a
        elif n[i] == 'b':
            count_b = count_a + 2*count_b
        else:
            count_c = count_b + 2*count_c
    print(count_c)
