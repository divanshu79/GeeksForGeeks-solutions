def get_all_substrings(input_string):
    length = len(input_string)
    return [(len(input_string[i:j+1]), input_string[i:j+1]) for i in range(length) for j in range(i,length)]


st = get_all_substrings('AMBYNZ')
print(st)
k = sorted(st)[::-1]
print(k)
