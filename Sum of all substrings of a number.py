def get_all_substrings(s):
    length = len(s)
    return (int(s[i: j]) for i in range(length) for j in range(i + 1, length + 1))


for _ in range(int(input())):
    n = input()
    print(sum(get_all_substrings(n)))
