for _ in range(int(input())):
    sorted_string = input()
    # sorted_string = sorted(set(string))

    max_string = ''
    ASCII = 0
    res_max_string = ''
    RES_ASCII = 0
    max_value = 0
    difference = 0
    for i in range(len(sorted_string)):
        if max_string == '':
            try:
                difference = abs(ord(sorted_string[i]) - ord(sorted_string[i + 1]))
            except:
                pass
        try:
            if abs(ord(sorted_string[i]) - ord(sorted_string[i + 1])) == difference:
                max_string += sorted_string[i]
                ASCII += ord(sorted_string[i])
            else:
                if len(max_string)+1 >= max_value and (ASCII + ord(sorted_string[i])) > RES_ASCII:
                    res_max_string = max_string + sorted_string[i]
                    max_value = len(res_max_string)
                    RES_ASCII = ASCII + ord(sorted_string[i])
                max_string = ''
                difference = abs(ord(sorted_string[i+2]) - ord(sorted_string[i + 1]))
                ASCII = 0
        except:
            if len(max_string)+1 >= len(res_max_string) and (ASCII + ord(sorted_string[i])) > RES_ASCII:
                res_max_string = max_string + sorted_string[i]
                RES_ASCII = ASCII + ord(sorted_string[i])
    print(res_max_string[::-1])
