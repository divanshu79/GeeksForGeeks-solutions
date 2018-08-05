from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    list_str = list(map(str, input().split()))
    string = input()
    def_dict = defaultdict(str)
    count_char = defaultdict(int)

    ans = ''

    for i in range(len(string)):
        count_char[string[i]] += 1
        for j in range(n):
            if string[i] in list_str[j] and list_str[j].count(string[i]) >= count_char[string[i]]:
                def_dict[list_str[j]] += string[i]

    for i in range(n):
        if len(def_dict[list_str[i]]) == len(list_str[i]):
            k = list_str[i]
            if len(k) > len(ans):
                ans = k
    print(ans)
