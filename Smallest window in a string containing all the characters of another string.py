from collections import defaultdict

for _ in range(int(input())):
    string = input()
    sub_str = input()
    def_dict = defaultdict(int)
    arr = []
    for i in range(len(sub_str)):
        def_dict[sub_str[i]] += 1

    