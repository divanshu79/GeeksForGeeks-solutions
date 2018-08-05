def consecutive_groups(iterable):
    s = tuple(iterable)
    seen = set()
    for size in range(1, len(s)+1):
        for index in range(len(s)+1-size):
            slc = iterable[index:index+size]
            if slc not in seen:
                seen.add(slc)
                yield slc


def difference(i,j):
    return abs(ord(i)-ord(j))


def list_set(s):
    s = list(set(s))
    new_string = ''
    for i in s:
        new_string += i
    return new_string


for _ in range(int(input())):
    string = input()
    # string = list_set(string)
    all_substring = list(consecutive_groups(string))[::-1]
    print(all_substring)

    max_string = ''
    ASCII = 0
    res_max_string = ''
    res_ASCII = 0
    max_len = 0
    diff = 0
    flag = 0

    for k in range(len(all_substring)):
        i = sorted(all_substring[k])
        # if i == 'ADGJ':
        i = list_set(i)
        print(i)
        for j in range(len(i)):
            if max_string == '':
                try:
                    diff = difference(i[j], i[j+1])
                    max_string = i
                    ASCII += ord(i[j])
                    flag = 0
                except:
                    res_max_string = i
                    flag = 0
                    break
            else:
                try:
                    if difference(i[j], i[j+1]) == diff:
                        ASCII += ord(i[j])
                        flag = 0
                    else:
                        max_string = ''
                        ASCII = 0
                        flag = 1
                        break
                except:
                    ASCII += ord(i[j])
                    flag = 0
        try:
            if flag == 0 and len(i) > len(all_substring[k+1]) and len(i) > max_len:
                print(i)
                break
            elif flag == 0 and len(i) == len(all_substring[k+1]):
                if ASCII > res_ASCII:
                    res_max_string = i
                    max_len = len(res_max_string)
                    res_ASCII = ASCII
                max_string = ''
                ASCII = 0
            elif flag == 0 and len(i) > len(all_substring[k+1]) and len(i) == max_len:
                if res_ASCII > ASCII:
                    print(res_max_string)
                    break
                elif res_ASCII < ASCII:
                    print(max_string)
                    break
        except:
            if len(i) > max_len:
                print(i)
                break
            elif len(i) == max_len:
                if ASCII > res_ASCII:
                    print(i)
                    break
                elif res_ASCII > ASCII:
                    print(res_max_string)
                    break
            elif len(i) < max_len:
                print(res_max_string)
                break
