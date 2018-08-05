from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    list_str = list(map(str, input().split()))
    string = input()

    def_dict = defaultdict(int)

    for i in range(n):
        def_dict[list_str[i]] = 1

    list_words = []
    word = ''

    for i in range(len(string)):
        word += string[i]
        if def_dict[word] == 1:
            list_words.append(word)
            word = ''
        else:
            kk = ''
            for j in range(len(list_words)-1, -1, -1):
                kk += list_words[j] + word
                if def_dict[kk] == 1:
                    list_words.append(kk)
                    word = ''
    if len(word) == 0:
        print(1)
    else:
        print(0)
